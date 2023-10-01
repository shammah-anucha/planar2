from datetime import datetime
from typing import Optional
from urllib import response
from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Response(Enum):
    Accept: str = "Accept"
    Decline: str = "Decline"


class RosterBase(BaseModel):
    pass


class RosterCreate(RosterBase):
    Firstname: Optional[str]
    Lastname: Optional[str]


class RosterUpdate(RosterBase):
    user_id: UUID
    event_id: UUID
    sender_id: UUID
    userrole_id: Optional[int]
    role: Optional[str]
    created_at: datetime
    Firstname: str
    Lastname: str
    response: Optional[str]
    response_date: Optional[datetime]


class Roster(RosterBase):
    roster_id: int
    user_id: UUID
    event_id: UUID
    sender_id: UUID
    userrole_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True


class RosterInDB(RosterBase):
    roster_id: int
    user_id: UUID
    event_id: UUID
    sender_id: UUID
    userrole_id: Optional[int]
    role: Optional[str]
    created_at: datetime
    Firstname: str
    Lastname: str
    response: Optional[str]
    response_date: Optional[datetime]

    class Config:
        orm_mode = True
