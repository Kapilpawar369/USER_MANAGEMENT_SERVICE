# services/users/routes.py
# Purpose: FastAPI router for user endpoints.
# Imported by: api/user/v1.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.users import service as user_service, schemas as user_schemas
from core.database.session import get_db
from services.auth.jwt import service as jwt_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=user_schemas.UserRead, status_code=status.HTTP_201_CREATED)
def register(user_in: user_schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        user = user_service.create_user(db, user_in)
        return user
    except Exception as exc:
        # Convert known exceptions to HTTP responses
        from core.common.exceptions import ConflictError

        if isinstance(exc, ConflictError):
            raise HTTPException(status_code=409, detail=str(exc))
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/login", response_model=user_schemas.TokenResponse)
def login(user_in: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # Use email + password to authenticate and return JWT
    user = user_service.get_user_by_email(db, user_in.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    from core.common.utils import verify_password

    if not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = jwt_service.create_access_token(subject=str(user.id))
    return {"access_token": access_token}
