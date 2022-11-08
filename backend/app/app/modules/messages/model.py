from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from ....app.modules.common.db.base_class import Base

from sqlalchemy import Column, Integer, ForeignKey


class Messages(Base):
    __tablename__ = "messages"

    msg_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.user_id"), nullable=False)
    message = Column(String, nullable=True)
