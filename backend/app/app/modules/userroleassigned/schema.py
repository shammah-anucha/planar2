from pydantic import BaseModel
from uuid import UUID


class UserRoleAssignedBase(BaseModel):
    id: int


class UserRoleAssignedCreate(UserRoleAssignedBase):
    pass


class UserRoleAssignedUpdate(UserRoleAssignedBase):
    pass


class UserRoleAssigned(UserRoleAssignedBase):
    user_id: UUID
    userrole_id: int
    Firstname: str
    Lastname: str

    class Config:
        orm_mode = True
