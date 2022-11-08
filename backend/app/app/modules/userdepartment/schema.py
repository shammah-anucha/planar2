from pydantic import BaseModel
from uuid import UUID


class UserDepartmentBase(BaseModel):
    userdept_id: int


class UserDepartmentCreate(UserDepartmentBase):
    pass


class UserDepartmentUpdate(UserDepartmentBase):
    pass


class UserDepartment(UserDepartmentBase):
    dept_id: int
    user_id: UUID

    class Config:
        orm_mode = True
