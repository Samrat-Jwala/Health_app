from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # plaintext, to be hashed later

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True