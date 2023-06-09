from sqlalchemy.orm import Session

import helper
from models import Run
from datetime import datetime, timedelta
from sqlalchemy import and_, func


def get_all_runs(db: Session):
    now = datetime.now()
    today = datetime.now().date()
    runs = db.query(Run).filter(
        and_(
            func.date(Run.scheduled_end_time) == today,
            Run.scheduled_end_time > now,
            Run.vehicle_id <= 21
        )
    ).all()

    # Increment scheduled_start_time and scheduled_end_time
    for run in runs:
        run.scheduled_start_time += timedelta(hours=2)
        run.scheduled_end_time += timedelta(hours=2)
        run.vehicle_id = helper.rename_vehicle(run.vehicle_id)

    return runs


def get_runs_by_run_name(db: Session, run_name: str):
    today = datetime.now().date()
    runs = db.query(Run).filter(
        and_(func.date(Run.scheduled_end_time) == today, Run.vehicle_id <= 21, Run.name == run_name)).all()

    # Increment scheduled_start_time and scheduled_end_time
    for run in runs:
        run.scheduled_start_time += timedelta(hours=2)
        run.scheduled_end_time += timedelta(hours=2)
        run.vehicle_id = helper.rename_vehicle(run.vehicle_id)

    return runs
