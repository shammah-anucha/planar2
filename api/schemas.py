from datetime import date, time
from typing import Any, List, Union, Optional
from pydantic import BaseModel, EmailStr, HttpUrl
from sqlalchemy.ext.declarative import as_declarative, declared_attr


class Token(BaseModel):
    access_token: str
    token_type: str


# class TokenData(BaseModel):
#     username: Union[str, None] = None


class TokenPayload(BaseModel):
    sub: Optional[int] = None


# events
class EventBase(BaseModel):
    name: str
    time: time
    location: str
    description: str
    date: date
    host: str
    # tags: Optional[List[str]]
    # image:Optional[HttpUrl]


class EventCreate(EventBase):
    pass


class Event(EventBase):
    event_id: int
    # user_id: int

    class Config:
        orm_mode = True


class RosterBase(BaseModel):
    pass


class RosterCreate(RosterBase):
    pass


class Roster(RosterBase):
    roster_id: int
    event_id: int
    user_id: int
    Firstname: Union[str, None]
    Lastname: Union[str, None]

    class Config:
        orm_mode = True


# users
# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    username: Union[str, None]
    Firstname: Union[str, None]
    Lastname: Union[str, None]
    D_O_B: Union[date, None]
    country_of_residence: Union[str, None]
    phone: Optional[Union[str, None]]
    is_admin: Union[bool, None] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


# unavailability
class UnavailabilityBase(BaseModel):
    start_date: date
    end_date: date


class Unavailability(UnavailabilityBase):
    aval_id: int

    class Config:
        orm_mode = True


class UnavailabilityCreate(UnavailabilityBase):
    pass


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


class InviteStatus(BaseModel):
    pass


class InviteUser(BaseModel):
    date_of_invite: date
    date_of_response: date


class DepartmentBase(BaseModel):
    deptname: str


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):
    dept_id: int

    class Config:
        orm_mode = True


# db
@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
