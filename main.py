# main.py
# Purpose: Application entrypoint. Creates FastAPI app, includes routers, and creates DB tables.
# Imported by: run server (uvicorn main:app --reload)

from fastapi import FastAPI, HTTPException
from core.config import settings
from core.connections import database as db_conn  # ensures engine/import side-effects not required
from core.database.session import get_db
from api.user.v1 import api_router
from core.connections.database import engine
from core.connections.database import Base
import services.users.models  # Ensures models are imported for metadata.create_all (or alembic autogenerate)

app = FastAPI(title=settings.APP_NAME)

# Include versioned API
app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
def on_startup():
    # Create tables automatically for simple setups (use Alembic in production)
    Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


# Global exception handler example (simple)
@app.exception_handler(Exception)
def generic_exception_handler(request, exc):
    # For production, log the exception and return generic message
    return HTTPException(status_code=500, detail=str(exc))
