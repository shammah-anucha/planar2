from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ...app.db.base_class import Base

if TYPE_CHECKING:
    from .unavailability import Unavailabilities


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    username = Column(String, index=True)
    Firstname = Column(String, index=True)
    Lastname = Column(String, index=True)
    D_O_B = Column(Date, index=True)
    country_of_residence = Column(String, index=True)
    phone = Column(String, index=True)
    disabled = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    events = relationship("Roster")
    unavailabilities = relationship("Unavailabilities", back_populates="user")
