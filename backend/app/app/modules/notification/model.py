from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base

from sqlalchemy import Column, Integer, Date, ForeignKey, Time


class Notification(Base):
    __tablename__ = "notification"

    notification_id = Column(Integer, primary_key=True, index=True)
    to_user = Column(Integer, ForeignKey("users.user_id"))
    from_user = Column(Integer, ForeignKey("users.user_id"))
    # accept = Column(String)
    # decline = Column(String)
    # date = Column(Date, default=datetime.today())
    # user_has_seen = Column(Boolean, default=False)
