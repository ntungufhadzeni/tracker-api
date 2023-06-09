from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import os
import crud
import schemas
import requests
from database import SessionLocal
from datetime import timedelta

base_url = os.getenv("TRACKER_URL")

app = FastAPI()


def rename_vehicle(vehicle_id):
    vehicle_id = int(vehicle_id)
    if vehicle_id < 10:
        return '00' + str(vehicle_id)
    elif vehicle_id >= 10:
        return '0' + str(vehicle_id)
    
    
def get_tracker_id(vehicle_id: str):
    res = requests.get(f'{base_url}/devices', auth=(os.getenv("TRACKER_USERNAME"), os.getenv("TRACKER_PASSWORD")))
    devices = res.json()
    for device in devices:
        if device["name"] == vehicle_id:
            return device["id"]
    return None

def get_vehicle_position(tracker_id: int):
    res = requests.get(f'{base_url}/positions', auth=(os.getenv("TRACKER_USERNAME"), os.getenv("TRACKER_PASSWORD")))
    devices = res.json()
    for device in devices:
        if device["deviceId"] == tracker_id:
            return device["latitude"], device["longitude"]
    return None, None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/runs", response_model=list[schemas.Run])
async def get_all_runs(db: Session = Depends(get_db)):
    runs = crud.get_all_runs(db)
    for run in runs:
        run.scheduled_start_time = run.scheduled_start_time + timedelta(hours=2)
        run.scheduled_end_time = run.scheduled_end_time + timedelta(hours=2)
        run.vehicle_id = rename_vehicle(run.vehicle_id)
        run.tracker_id = get_tracker_id(run.vehicle_id)
        run.latitude, run.longitude = get_vehicle_position(run.tracker_id)
    return runs


@app.get("/api/v1/runs/{name}", response_model=list[schemas.Run])
async def get_runs_by_run_name(name: str, db: Session = Depends(get_db)):
    name = ' '.join(name.split("-"))
    runs = crud.get_runs_by_run_name(db, name)
    for run in runs:
        run.scheduled_start_time = run.scheduled_start_time + timedelta(hours=2)
        run.scheduled_end_time = run.scheduled_end_time + timedelta(hours=2)
        run.vehicle_id = rename_vehicle(run.vehicle_id)
        run.tracker_id = get_tracker_id(run.vehicle_id)
        run.latitude, run.longitude = get_vehicle_position(run.tracker_id)
    return runs
