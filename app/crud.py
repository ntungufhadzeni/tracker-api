from sqlalchemy.orm import Session
from models import Run
from datetime import datetime
from sqlalchemy import and_, func


def get_all_runs(db: Session):
    now = datetime.now()
    today = datetime.now().date()
    return db.query(Run).filter(and_(func.date(Run.scheduled_end_time) == today, Run.scheduled_end_time > now, Run.vehicle_id <= 21)).all()

def get_runs_by_run_name(db: Session, run_name: str):
    today = datetime.now().date()
    return db.query(Run).filter(and_(func.date(Run.scheduled_end_time) == today, Run.vehicle_id <= 21, Run.name.startswith(run_name))).all()


def get_run_by_id(db: Session, run_id: int):
    return db.query(Run).filter(Run.id == run_id).first()