from typing import Optional

from pydantic import BaseModel


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


class EventInDBBase(EventBase):
    event_id: int
    # user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Event(EventInDBBase):
    pass


# Properties properties stored in DB
class EventInDB(EventInDBBase):
    pass
