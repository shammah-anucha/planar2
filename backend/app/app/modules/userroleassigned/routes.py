from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ....app.modules.common.db.session import get_db
from sqlalchemy.orm import Session
from ....app.modules.userroleassigned.schema import UserRoleAssigned
from ....app.modules.userroleassigned.crud import userrolesassigned

userroleassigned_router = APIRouter(
    prefix="/userrole", tags=["userrole"], dependencies=[Depends(get_db)]
)


# is it neccessary to create a schema for user_department
@userroleassigned_router.post(
    "/{userrole_id}/users/{user_id}", response_model=UserRoleAssigned
)
def assign_userrole(user_id: int, userrole_id: int, db: Session = Depends(get_db)):
    return userrolesassigned.assign_userrole(
        user_id=user_id, userrole_id=userrole_id, db=db
    )
    # TODO avoid repeating the same entry


@userroleassigned_router.get("/{userrole_id}")
def get_user_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return userrolesassigned.get_all_userrolesassigned(db, skip=skip, limit=limit)
