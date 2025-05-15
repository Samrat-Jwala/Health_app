from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.appointment import AppointmentCreate, AppointmentResponse
from app.models.appointment import Appointment
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppointmentResponse)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    new_appointment = Appointment(
        user_id=appointment.user_id,
        reason=appointment.reason,
        date=appointment.date,
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

@router.get("/", response_model=List[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()