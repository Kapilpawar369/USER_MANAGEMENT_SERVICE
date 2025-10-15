from sqlalchemy.orm import sessionmaker,Session
from core.connections.database import engine

# core/database/session.py
# Purpose: Create SessionLocal and provide get_db() dependency for FastAPI.
# Imported by: services/* modules (for DB access) and routes.

from sqlalchemy.orm import sessionmaker, Session
from core.connections.database import engine

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def get_db():
    """
    FastAPI dependency that yields a DB session and ensures it is closed.
    Usage: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
