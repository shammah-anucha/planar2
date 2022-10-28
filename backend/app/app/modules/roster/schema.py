from typing import Optional

from pydantic import BaseModel


class RosterBase(BaseModel):
    roster_id: int


class RosterCreate(RosterBase):
    pass


class RosterUpdate(RosterBase):
    pass


class Roster(RosterBase):
    user_id: int
    event_id: int
    Firstname: Optional[str]
    Lastname: Optional[str]

    class Config:
        orm_mode = True
