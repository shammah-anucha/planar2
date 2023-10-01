from sqlalchemy import Column, Integer, String
from ....app.modules.common.db.base_class import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class UserRolesAssigned(Base):
    __tablename__ = "userrolesassigned"

    id = Column(Integer, primary_key=True, index=True)
    userrole_id = Column(Integer, unique=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=False)
