from typing import Optional, List
from datetime import date
from .events import Event
from .unavailability import Unavailability

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: Optional[str]
    Firstname: Optional[str]
    Lastname: Optional[str]
    D_O_B: Optional[date]
    country_of_residence: Optional[str]
    phone: Optional[str]
    is_admin: Optional[bool] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    user_id: int
    disabled: bool
    event: List[Event] = []
    unavailabilities: List[Unavailability] = []

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
