from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ...app.db.base_class import Base

# from ...app.models.unavailability import Unavailabilities
from sqlalchemy import Column, Integer, Date, ForeignKey, Time

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


class UserDepartment(Base):
    __tablename__ = "userdepartment"

    userdept_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))


class Roster(Base):
    __tablename__ = "rosters"

    roster_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.user_id"))
    event_id = Column(ForeignKey("events.event_id"))
    Firstname = Column(String)
    Lastname = Column(String)
    event = relationship("Event")


class Notification(Base):
    __tablename__ = "notification"

    notification_id = Column(Integer, primary_key=True, index=True)
    to_user = Column(Integer, ForeignKey("users.user_id"))
    from_user = Column(Integer, ForeignKey("users.user_id"))
    # accept = Column(String)
    # decline = Column(String)
    # date = Column(Date, default=datetime.today())
    # user_has_seen = Column(Boolean, default=False)


class Messages(Base):
    __tablename__ = "messages"

    msg_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    message = Column(String)


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String, index=True)
    time = Column(Time, index=True)
    location = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(Date, index=True)
    host = Column(String, index=True)


class Departments(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, index=True)
    deptname = Column(String, index=True)
