from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Date, ForeignKey, String, Boolean
from app.db.base_class import Base

from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .events import Event  # noqa: F401


class Roster(Base):
    __tablename__ = "rosters"

    roster_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.user_id"))
    event_id = Column(ForeignKey("events.event_id"))
    Firstname = Column(String)
    Lastname = Column(String)
    event = relationship("Event")
