from typing import TYPE_CHECKING
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base

# from ....app.modules.events.model import event_volunteers
import uuid

if TYPE_CHECKING:
    from ....app.modules.unavailability.model import Unavailabilities

import uuid


class Users(Base):

    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    email = Column(String, unique=True)
    hashed_password = Column(String)
    username = Column(String)
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=False)
    D_O_B = Column(Date, nullable=False)
    nationality = Column(String, nullable=False)
    country_of_residence = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    country_code = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    unavailabilities = relationship("Unavailabilities", back_populates="user")
