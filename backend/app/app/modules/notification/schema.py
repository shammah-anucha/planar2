from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


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
    to_user: UUID
    from_user: UUID

    class Config:
        orm_mode = True
