from sqlalchemy import Column, Integer, String
from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer, ForeignKey


class UserRoles(Base):

    __tablename__ = "userroles"

    userrole_id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, index=True)
