from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base
from ....app.modules.users.model import Users
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, Date, ForeignKey, Time

if TYPE_CHECKING:
    from ....app.modules.users.model import Users


class Unavailabilities(Base):
    __tablename__ = "unavailabilities"

    aval_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    startdate = Column(Date, index=True)
    enddate = Column(Date, index=True)
    reason = Column(String, index=True)  # migrate
    user = relationship("Users", back_populates="unavailabilities")
