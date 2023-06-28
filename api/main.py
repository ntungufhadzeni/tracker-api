from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from redis import asyncio as aioredis
import crud
import helper
import schemas
from database import SessionLocal
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url(f"redis://redis", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="api:cache")


@app.get('/')
@cache(expire=60*60)
async def index():
    return {'Hello': 'Welcome to Leeto Tracker API. Add /docs to view API docs'}


@app.get("/api/v1/runs", response_model=list[schemas.Schedule])
@cache(expire=60*15)
async def get_all_runs(db: Session = Depends(get_db)):
    return crud.get_all_runs(db)


@app.get("/api/v1/runs/{name}", response_model=list[schemas.Run])
async def get_runs_by_run_name(name: str, db: Session = Depends(get_db)):
    name = ' '.join(name.split("-"))
    runs = crud.get_runs_by_run_name(db, name)
    for run in runs:
        run.latitude, run.longitude = helper.get_vehicle_position(run.vehicle_id)
    return runs
