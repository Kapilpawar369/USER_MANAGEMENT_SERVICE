# services/users/service.py
# Purpose: Business logic for users (create, get).
# Imported by: services/users/routes.py

from sqlalchemy.orm import Session
from core.common.exceptions import NotFoundError, ConflictError
from services.users import models, schemas
from core.common import utils


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user_in: schemas.UserCreate) -> models.User:
    # Check if email already exists
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise ConflictError("User with this email already exists")

    hashed = utils.hash_password(user_in.password)
    user = models.User(email=user_in.email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> models.User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise NotFoundError("User not found")
    return user
