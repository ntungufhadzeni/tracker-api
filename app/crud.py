from sqlalchemy.orm import Session
from models import Run
from datetime import datetime, timedelta
from sqlalchemy import and_


def get_runs(db: Session):
    now = datetime.now() - timedelta(hours=2)
    return db.query(Run).filter(and_(Run.scheduled_end_time > now, Run.vehicle_id != 38)).all()

def get_runs_by_route(db: Session, run_name: str):
    now = datetime.now() - timedelta(hours=2)
    return db.query(Run).filter(and_(Run.scheduled_end_time > now, Run.vehicle_id != 38, Run.name.startswith(run_name))).all()


def get_run_by_id(db: Session, run_id: int):
    return db.query(Run).filter(Run.id == run_id).first()