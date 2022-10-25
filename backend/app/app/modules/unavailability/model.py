from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base
from ....app.modules.users.model import Users

from sqlalchemy import Column, Integer, Date, ForeignKey, Time

if TYPE_CHECKING:
    from ....app.modules.users.model import Users


class Unavailabilities(Base):
    __tablename__ = "unavailabilities"

    aval_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    user = relationship("Users", back_populates="unavailabilities")
