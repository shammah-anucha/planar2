from datetime import date

from pydantic import BaseModel


class UnavailabilityBase(BaseModel):
    start_date: date
    end_date: date


class Unavailability(UnavailabilityBase):
    aval_id: int

    class Config:
        orm_mode = True


class UnavailabilityCreate(UnavailabilityBase):
    pass


class UnavailabilityUpdate(UnavailabilityBase):
    pass
