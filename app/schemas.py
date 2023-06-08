from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Run(BaseModel):
    name: str
    scheduled_start_time: datetime
    scheduled_end_time: datetime
    vehicle_id: str
    driver_id: int
    vehicle_latitude: Optional[float] = None
    vehicle_longitude: Optional[float] = None
    tracker_id: Optional[int] = None

    class Config:
        orm_mode = True




