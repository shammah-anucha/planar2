from pydantic import BaseModel
from datetime import date, datetime


class NotificationBase(BaseModel):
    # accept: str
    # decline: str
    # received_date: date
    # user_has_seen: bool
    notification_id: int


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(NotificationBase):
    pass


class Notification(NotificationBase):
    to_user: int
    from_user: int

    class Config:
        orm_mode = True
