# services/users/schemas.py
# Purpose: Pydantic models for request/response validation for users.
# Imported by: routes and services

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
