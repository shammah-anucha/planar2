from sqlalchemy import Column, Integer, String
from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer


class Departments(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, index=True)
    deptname = Column(String, index=True)
