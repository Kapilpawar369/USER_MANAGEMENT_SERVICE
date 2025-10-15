# core/config.py
# Purpose: Central application settings (environment-backed).
# Imported by: core/connections/database.py, services/auth/jwt/service.py, main.py

# Old (v1.x)


# New (v2.x)
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    APP_NAME: str = "user_management"
    DEBUG: bool = True
    # Default to a local sqlite for convenience - override with env var for production
    DATABASE_URL: str = "sqlite:///./user_management."
    # JWT settings
    JWT_SECRET_KEY: str = "please-change-me"  # override with env in production
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day by default

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
