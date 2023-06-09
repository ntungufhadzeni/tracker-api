from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Run(BaseModel):
    name: str
    scheduled_start_time: datetime
    scheduled_end_time: datetime
    vehicle_id: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    tracker_id: Optional[int] = None

    class Config:
        orm_mode = True




