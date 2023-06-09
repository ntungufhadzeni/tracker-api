from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.orm import column_property
from datetime import timedelta
from database import Base


class Run(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    scheduled_start_time = Column(DateTime)
    scheduled_end_time = Column(DateTime)
    vehicle_id = Column(Integer)
    