from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base

# from ...app.models.unavailability import Unavailabilities
from sqlalchemy import Column, Integer, Date, ForeignKey, Time

# if TYPE_CHECKING:
#     from ...app.models.unavailability import Unavailabilities


class Departments(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, index=True)
    deptname = Column(String, index=True)
