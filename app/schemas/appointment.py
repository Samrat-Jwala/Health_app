from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentBase(BaseModel):
    reason: Optional[str] = None
    date: Optional[datetime] = None  # default will be set server-side

class AppointmentCreate(AppointmentBase):
    user_id: int

class AppointmentResponse(AppointmentBase):
    id: int
    user_id: int

    class Config:
        from_attributes=True