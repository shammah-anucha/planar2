from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer, Date, ForeignKey, Time


class Roster(Base):
    __tablename__ = "rosters"

    roster_id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), nullable=False)
    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    event_id = Column(ForeignKey("event.event_id"), nullable=False)
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=False)
    response = Column(String, nullable=True)
    response_date = Column(DateTime(timezone=True), nullable=True)
