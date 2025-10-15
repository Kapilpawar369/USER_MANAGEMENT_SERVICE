# api/user/v1.py
# Purpose: Versioned router aggregator for user-related APIs.
# Imported by: main.py

from fastapi import APIRouter
from services.users.routes import router as users_router

api_router = APIRouter()
api_router.include_router(users_router)
