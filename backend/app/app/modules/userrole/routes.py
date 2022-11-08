from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ....app.modules.common.db.session import get_db
from sqlalchemy.orm import Session
from .schema import UserRole, UserRoleCreate
from ....app.modules.userdepartment.schema import UserDepartment
from ....app.modules.userroleassigned.crud import userrolesassigned
from ....app.modules.userrole.crud import userroles
from ....app.modules.users.crud import user

userrole_router = APIRouter(
    prefix="/userrole", tags=["userrole"], dependencies=[Depends(get_db)]
)

# departments
@userrole_router.post("/", response_model=UserRole)
def create_userrole(departments: UserRoleCreate, db: Session = Depends(get_db)):
    return userroles.create_userrole(db=db, obj_in=departments)


@userrole_router.get("/", response_model=List[UserRole])
def get_userroles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return userroles.get_multi_userroles(db, skip=skip, limit=limit)
