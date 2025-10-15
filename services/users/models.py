# services/users/models.py
# Purpose: SQLAlchemy ORM models for users.
# Imported by: Alembic (for autogenerate), services/users/service.py

from sqlalchemy import Column, Integer, String, Boolean
from core.connections.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
