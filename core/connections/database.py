from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from core.config import settings

engine=create_engine(settings.DATABASE_URL,future=True,echo=False)

Base=declarative_base()