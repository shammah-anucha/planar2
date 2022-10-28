from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer, Date, ForeignKey, Time


class Roster(Base):
    __tablename__ = "rosters"

    roster_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.user_id"))
    event_id = Column(ForeignKey("events.event_id"))
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=False)
