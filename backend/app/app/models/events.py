from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date

from app.db.base_class import Base


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
