from pydantic import BaseModel


class UserDepartmentBase(BaseModel):
    userdept_id: int


class UserDepartmentCreate(UserDepartmentBase):
    pass


class UserDepartmentUpdate(UserDepartmentBase):
    pass


class UserDepartment(UserDepartmentBase):
    dept_id: int
    user_id: int

    class Config:
        orm_mode = True
