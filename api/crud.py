from sqlalchemy.orm import Session
from models import Run
from datetime import datetime, timedelta
from sqlalchemy import and_, func


def get_all_runs(db: Session):
    now = datetime.now() - timedelta(hours=2)
    today = datetime.now().date()
    return db.query(Run).filter(
        and_(func.date(Run.scheduled_end_time) == today, Run.scheduled_end_time > now, Run.vehicle_id <= 21)).all()


def get_runs_by_run_name(db: Session, run_name: str):
    today = datetime.now().date()
    return db.query(Run).filter(
        and_(func.date(Run.scheduled_end_time) == today, Run.vehicle_id <= 21, Run.name == run_name)).all()
