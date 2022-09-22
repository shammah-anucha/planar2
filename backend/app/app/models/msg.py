from sqlalchemy import Column, Integer, String, ForeignKey
from ...app.db.base_class import Base


class Messages(Base):
    __tablename__ = "messages"

    msg_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    message = Column(String)
