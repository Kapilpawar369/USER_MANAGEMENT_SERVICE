# services/auth/jwt/routes.py
# Purpose: Optional separate auth router if you want dedicated auth endpoints.
# Note: We implemented login in users/routes.py for simplicity.
# This file is included for completeness; you can import its router in main if desired.

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

# Example endpoints could be added here (login, refresh). The project uses users/routes.login already.
