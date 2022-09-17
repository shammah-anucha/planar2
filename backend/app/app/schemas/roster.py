from typing import Optional

from pydantic import BaseModel


class RosterBase(BaseModel):
    pass


class RosterCreate(RosterBase):
    pass


class Roster(RosterBase):
    roster_id: int
    event_id: int
    user_id: int
    Firstname: Optional[str]
    Lastname: Optional[str]

    class Config:
        orm_mode = True
