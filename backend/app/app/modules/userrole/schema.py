from pydantic import BaseModel


class UserRoleBase(BaseModel):
    role: str


class UserRoleCreate(UserRoleBase):
    pass


class UserRoleUpdate(UserRoleBase):
    pass


class UserRole(UserRoleBase):
    userrole_id: int

    class Config:
        orm_mode = True
