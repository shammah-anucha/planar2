from sqlalchemy import Column, Integer, String
from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer, ForeignKey


class UserRolesAssigned(Base):

    __tablename__ = "userrolesassigned"

    id = Column(Integer, primary_key=True, index=True)
    userrole_id = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=False)
