from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Integer, Date, ForeignKey, Time


class RosterShort(Base):
    __tablename__ = "roster_short"

    rostershort_id = Column(Integer, primary_key=True, index=True)
    roster_id = Column(Integer, ForeignKey("rosters.roster_id"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=True)
    role = Column(String, nullable=True)
    title = Column(String, nullable=False)
    event_date = Column(String, nullable=True)
    time = Column(String, nullable=False)
