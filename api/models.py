from email.policy import default
from enum import unique
from typing import List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, Table
from sqlalchemy.orm import relationship, deferred
from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from database import Base


class Roster(Base):
    __tablename__ = "rosters"

    roster_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.user_id"))
    event_id = Column(ForeignKey("events.event_id"))
    Firstname = Column(String)
    Lastname = Column(String)
    event = relationship("Event")
    # Firstname = Column(String, ForeignKey("users.Firstname"))
    # Lastname = Column(String, ForeignKey("users.Lastname"))
    # date = Column(Date, index = True)
    # time = Column(Time, index = True)

    # user = relationship("Event", back_populates="events")
    # owner = relationship("User", back_populates = "events")


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

    # events = relationship("Event", secondary=roster_table)

    # id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")


class Event(Base):
    __tablename__ = "events"

    # id = Column(Integer, primary_key=True, index = True)
    # title = Column(String, index=True)
    # description = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates = "items")

    event_id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String, index=True)
    time = Column(Time, index=True)
    location = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(Date, index=True)
    host = Column(String, index=True)
    # tags = Column(List[String])
    # image = deferred(Column(Binary))

    # owner = relationship("User", back_populates = "events")


class Unavailabilities(Base):
    __tablename__ = "unavailabilities"

    aval_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    user = relationship("User", back_populates="unavailabilities")
    # Firstname = Column(String, ForeignKey("users.Firstname"))
    # Lastname = Column(String, ForeignKey("users.Lastname"))
    # available_days = Column(Date, index = True)


# class UpcomingEvents(Base):
#     __tablename__ = "upcoming_events"

#     id = Column(Integer, primary_key = True, index=True)
#     event_id = Column(Integer, ForeignKey("events.event_id"))
#     event_name = Column(String)
#     date = Column(Date, index = True)


class Departments(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, index=True)
    deptname = Column(String, index=True)


class UserDepartment(Base):
    __tablename__ = "userdepartment"

    userdept_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))


class Notification(Base):
    __tablename__ = "notification"

    notification_type = Column(Integer, primary_key=True, index=True)
    to_user = Column(Integer, ForeignKey("users.user_id"))
    from_user = Column(Integer, ForeignKey("users.user_id"))
    accept = Column(String)
    decline = Column(String)
    date = Column(Date, default=datetime.today())
    user_has_seen = Column(Boolean, default=False)


# class DeletedUsers(Base):
#     __tablename__ = "deleted_users"

#     id = Column(Integer, primary_key = True, index=True)
#     user_id = Column(Integer, ForeignKey("users.user_id"))
#     reason = Column(String(250), index=True)
#     date = Column(Date, index = True)

# class DeletedEvents(Base):
#     __tablename__ = "deleted_events"

#     id = Column(Integer, primary_key = True, index=True)
#     event_id = Column(Integer, ForeignKey("events.event_id"))
#     reason = Column(String(250), index=True)
#     date = Column(Date, index = True)

# class InviteUser(Base):
#     __tablename__ = "deleted_events"
