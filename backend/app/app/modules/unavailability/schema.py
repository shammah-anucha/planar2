from datetime import date
from uuid import UUID

from pydantic import BaseModel


class UnavailabilityBase(BaseModel):
    startdate: date
    enddate: date
    reason: str
    user_id: UUID


class Unavailability(UnavailabilityBase):
    aval_id: int

    class Config:
        orm_mode = True


class UnavailabilityCreate(UnavailabilityBase):
    pass


class UnavailabilityUpdate(UnavailabilityBase):
    pass
