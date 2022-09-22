from pydantic import BaseModel


class DepartmentBase(BaseModel):
    deptname: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(DepartmentBase):
    pass


class Department(DepartmentBase):
    dept_id: int

    class Config:
        orm_mode = True
