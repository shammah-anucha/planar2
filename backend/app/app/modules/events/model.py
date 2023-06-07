from sqlalchemy import Column, Integer, String, Date, Table, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = "event"

    event_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )
    title = Column(String, index=True)
    location = Column(String, index=True)
    location_url = Column(String, index=True)
    eventdate = Column(String, index=True)
    time = Column(String, index=True)
    imageUrl = Column(String, index=True)
    host = Column(String, index=True)
    # tags = Column(String)
