from typing import Optional, List, Union
from datetime import date
from ..events.schema import Event
from ..unavailability.schema import Unavailability

from pydantic import BaseModel, EmailStr
from ...modules.common.utils.country_code import CountryCodes


class UserBase(BaseModel):
    email: EmailStr
    username: Optional[str]
    Firstname: str
    Lastname: str
    D_O_B: date
    country_of_residence: Optional[str]
    nationality: str
    country_code: CountryCodes
    phone: int
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
    # assigned_events: int
    unavailabilities: List[Unavailability] = []

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
