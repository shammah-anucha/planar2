from sqlalchemy import Column, Integer, String, ForeignKey
from ...app.db.base_class import Base


class UserDepartment(Base):
    __tablename__ = "userdepartment"

    userdept_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))
