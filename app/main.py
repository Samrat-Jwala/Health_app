from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.endpoints.appointments import router as appointment_router
from app.api.v1.endpoints.user import router as users_router


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the Health Checkup API"}

app.include_router(appointment_router, prefix="/appointments", tags=["Appointments"])
app.include_router(users_router, prefix="/users", tags=["Users"])
