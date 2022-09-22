from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from ...app.db.base_class import Base

if TYPE_CHECKING:
    from .users import User


class Unavailabilities(Base):
    __tablename__ = "unavailabilities"

    aval_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    user = relationship("User", back_populates="unavailabilities")
