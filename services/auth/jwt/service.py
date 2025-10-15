# services/auth/jwt/service.py
# Purpose: JWT token creation & verification.
# Imported by: routes (login), dependencies for protected endpoints

from datetime import datetime, timedelta
from jose import jwt, JWTError
from core.config import settings
from typing import Optional


def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Returns a signed JWT token with 'sub' claim set to subject (usually user id).
    """
    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = datetime.utcnow() + expires_delta
    payload = {"sub": subject, "exp": expire}
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token


def verify_access_token(token: str) -> dict:
    """
    Verifies the token and returns payload.
    Raises JWTError on invalid token.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as exc:
        raise
