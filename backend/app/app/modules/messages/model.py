from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.modules.common.db.base_class import Base

# from ...app.models.unavailability import Unavailabilities
from sqlalchemy import Column, Integer, Date, ForeignKey, Time

# if TYPE_CHECKING:
#     from ...app.models.unavailability import Unavailabilities


class Messages(Base):
    __tablename__ = "messages"

    msg_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    message = Column(String)
