from fastapi import HTTPException, Depends, status
from xml.dom import ValidationErr
from api import models, crud
from sqlalchemy.orm import Session
from .schemas import TokenPayload, Base
from fastapi.security import OAuth2PasswordBearer
from typing import TypeVar
from jose import jwt, JWTError
from passlib.context import CryptContext
import secrets
from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


API_V1_STR: str = "/api/v1"
SECRET_KEY = secrets.token_urlsafe(32)
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{API_V1_STR}/login/access-token")

ALGORITHM = "HS256"

ModelType = TypeVar("ModelType", bound=Base)


# done
async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> models.User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationErr):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.get_user_id(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if crud.disabled(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_active_admin(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.is_admin(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
