# services/auth/jwt/schemas.py
# Purpose: Token request/response schemas used by auth endpoints.
# Imported by: routes

from pydantic import BaseModel


class TokenRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
