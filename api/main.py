from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import helper
import schemas
from database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {'Hello': 'Welcome to Leeto Tracker API. Add /docs to view API docs'}


@app.get("/api/v1/runs", response_model=list[schemas.Schedule])
async def get_all_runs(db: Session = Depends(get_db)):
    return crud.get_all_runs(db)


@app.get("/api/v1/runs/{name}", response_model=list[schemas.Run])
async def get_runs_by_run_name(name: str, db: Session = Depends(get_db)):
    name = ' '.join(name.split("-"))
    runs = crud.get_runs_by_run_name(db, name)
    for run in runs:
        run.latitude, run.longitude = helper.get_vehicle_position(run.vehicle_id)
    return runs
