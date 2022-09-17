from email import message
from multiprocessing import Event
from xml.dom import ValidationErr
from sqlalchemy.orm import Session
from api import models, schemas
from .schemas import TokenPayload, Base

from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional, TypeVar, Union, Any
from jose import jwt, JWTError
from passlib.context import CryptContext
import secrets
from .database import SessionLocal
import pdb


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


API_V1_STR: str = "/api/v1"
SECRET_KEY = secrets.token_urlsafe(32)
# 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{API_V1_STR}/login/access-token")

# SECRET_KEY = "32f5474dc85f616a51557603e4fc494ae8f73bdf67c799bfac577bb5686c1695c7"
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

ModelType = TypeVar("ModelType", bound=Base)
# def fake_hash_password(password: str):
#     return "fakehashed" + password


# all was put into a class --done till is_admin
# transferred
def disabled(user: models.User) -> bool:
    return user.disabled


# transferred
def is_admin(user: models.User) -> bool:
    return user.is_admin


# done - security.py
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user_id(db: Session, id: Any):
    return db.query(models.User).filter(models.User.user_id == id).first()


# done - security.py
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# pdb.set_trace()

# done - security.py
def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# transferred
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
    user = get_user_id(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# transferred
async def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if disabled(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# transferred
async def get_current_active_admin(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not is_admin(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user


# all was put into a class --done till is_admin
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# transferred
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        email=user.email,
        username=user.username,
        Firstname=user.Firstname,
        Lastname=user.Lastname,
        D_O_B=user.D_O_B,
        country_of_residence=user.country_of_residence,
        phone=user.phone,
        is_admin=user.is_admin,
        hashed_password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def update(db: Session, db_user: models.User, user: Union[UserUpdate, Dict[str, Any]]) -> models.User

# transferred
def authenticate_user(db: Session, email: str, password: str) -> Optional[models.User]:
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


# transferred
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


# def get_event_by_name(db: Session, name:str):
#     return db.query(models.Event).filter(models.Event.name==name).first()

# transferred
def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(
        name=event.name,
        time=event.time,
        location=event.location,
        description=event.description,
        date=event.date,
        host=event.host,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# def create_roster(db: Session, roster: schemas.RosterCreate, user_id: int, event_id: int, Firstname = str, Lastname = str):
#     db_event = models.Roster(user_id=user_id, event_id=event_id, Firstname=Firstname, Lastname=Lastname, roster=roster)
#     db.add(db_event)
#     db.commit()
#     db.refresh(db_event)
#     return db_event

# transferred
# TODO remove unavailable emails that have passed the time frame
def get_user_unavailable(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unavailabilities).offset(skip).limit(limit).all()


# transferred
def set_user_unavailable(db: Session, days: schemas.UnavailabilityCreate, user_id: int):
    db_unavalable_days = models.Unavailabilities(
        start_date=days.start_date, end_date=days.end_date, user_id=user_id
    )
    db.add(db_unavalable_days)
    db.commit()
    db.refresh(db_unavalable_days)
    return db_unavalable_days


# transferred
def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Departments(deptname=department.deptname)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


# transferred
def get_department(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Departments).offset(skip).limit(limit).all()


# transferred
def assign_department(db: Session, dept_id: int, user_id: int):
    db_user_dept = models.UserDepartment(user_id=user_id, dept_id=dept_id)
    db.add(db_user_dept)
    db.commit()
    db.refresh(db_user_dept)
    return db_user_dept


# transferred
def get_dept_id(db: Session, id: Any):
    return (
        db.query(models.Departments.dept_id)
        .filter(models.Departments.dept_id == id)
        .first()
    )


# transferred
def get_user_department(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserDepartment).offset(skip).limit(limit).all()


# transferred
def get_available_emails(db: Session):
    emails = []
    for email in (
        db.query(models.User.email).filter(models.User.unavailabilities == None).all()
    ):
        email = "\n".join(list(email))
        emails.append(email)
    return emails


# transferred
def get_email_in_department(dept_id: int, db: Session):
    emails = []
    for email, dept_id in (
        db.query(models.User.email, models.UserDepartment.dept_id)
        .filter(models.User.user_id == models.UserDepartment.user_id)
        .filter(models.UserDepartment.dept_id == dept_id)
        .all()
    ):
        email = "".join(list(email))
        emails.append(email)
    return emails


# send notifications

# transferred
def assign_message(db: Session, user_id: int):
    message = "You have been invited to serve"
    db_message = models.Messages(user_id=user_id, message=message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


# transferred
def send_notification(from_user: int, db: Session, to_user=int):
    admin = (
        db.query(models.User.is_admin)
        .filter(models.User.user_id == from_user)
        .filter(models.User.is_admin == "true")
        .first()
    )
    # if not user:
    #     raise HTTPException(status_code=)
    if admin:
        return assign_message(user_id=to_user, db=db)
    else:
        return "User doesn't have enough Priviledges"
