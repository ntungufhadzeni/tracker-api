from sqlalchemy import Column, String, Integer, DateTime

from database import Base


class Run(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    scheduled_start_time = Column(DateTime)
    scheduled_end_time = Column(DateTime)
    vehicle_id = Column(Integer)
    