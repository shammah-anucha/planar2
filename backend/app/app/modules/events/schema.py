from datetime import time, date

from pydantic import BaseModel
from uuid import UUID


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
    name: str


class EventUpdate(EventBase):
    pass


class Volunteer(BaseModel):
    event_id: int
    user_id: UUID


class EventInDBBase(EventBase):
    event_id: int
    # user_id: UUID
    # volunteer: UUID

    class Config:
        orm_mode = True


# Properties to return to client
class Event(EventInDBBase):
    pass


# Properties properties stored in DB
class EventInDB(EventInDBBase):
    pass
