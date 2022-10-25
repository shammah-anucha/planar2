from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

from ....app.modules.common.db.base_class import Base

from sqlalchemy import Column, Integer, Date, ForeignKey, Time


class UserDepartment(Base):
    __tablename__ = "userdepartment"

    userdept_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))
