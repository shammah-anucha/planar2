from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ...app.db.base_class import Base
from ...app.models.roster import Roster

# from ...app.models.unavailability import Unavailabilities
from sqlalchemy import Column, Integer, Date, ForeignKey

# if TYPE_CHECKING:
#     from ...app.models.unavailability import Unavailabilities


class Users(Base):

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


class Unavailabilities(Base):
    __tablename__ = "unavailabilities"

    aval_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    user = relationship("Users", back_populates="unavailabilities")
