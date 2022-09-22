from sqlalchemy import Column, Integer, Date, ForeignKey, String, Boolean
from ...app.db.base_class import Base
from datetime import datetime


class Notification(Base):
    __tablename__ = "notification"

    notification_type = Column(Integer, primary_key=True, index=True)
    to_user = Column(Integer, ForeignKey("users.user_id"))
    from_user = Column(Integer, ForeignKey("users.user_id"))
    accept = Column(String)
    decline = Column(String)
    date = Column(Date, default=datetime.today())
    user_has_seen = Column(Boolean, default=False)
