from sqlalchemy import Column, Integer, String, DateTime
from ....app.modules.common.db.base_class import Base
from . import schema
from sqlalchemy import Column, ForeignKey, Integer, Date, Time


class Responses(Base):
    __tablename__ = "response"

    response_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.user_id"))
    event_id = Column(ForeignKey("events.event_id"))
    response = Column(schema.Responses, index=True)
    response_date = Column(DateTime(timezone=True), nullable=False)
