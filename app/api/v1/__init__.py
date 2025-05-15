from fastapi import APIRouter
from app.api.v1.endpoints import user, appointments

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])