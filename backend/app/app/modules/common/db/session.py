from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .....app.modules.common.utils.core.config import settings
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
