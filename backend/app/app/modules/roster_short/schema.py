from datetime import datetime
from typing import Optional
from urllib import response
from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class RosterShortBase(BaseModel):
    pass


class RosterShortCreate(RosterShortBase):
    pass


class RosterShortUpdate(RosterShortBase):
    pass


class RosterShort(RosterShortBase):
    rostershort_id: int

    class Config:
        orm_mode = True


class RosterShortInDB(RosterShortBase):
    rostershort_id: int
    roster_id: Optional[int]
    user_id: Optional[UUID]
    role: Optional[str]
    title: str
    event_date: Optional[str]
    time: str

    class Config:
        orm_mode = True
