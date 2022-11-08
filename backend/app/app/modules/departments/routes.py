from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ....app.modules.common.db.session import get_db
from sqlalchemy.orm import Session
from .schema import Department, DepartmentCreate
from ....app.modules.userdepartment.schema import UserDepartment
from ....app.modules.userdepartment.crud import userdept
from ....app.modules.departments.crud import department
from ....app.modules.users.crud import user
from uuid import UUID

department_router = APIRouter(
    prefix="/departments", tags=["departments"], dependencies=[Depends(get_db)]
)

# departments
@department_router.post("/", response_model=Department)
def create_department(departments: DepartmentCreate, db: Session = Depends(get_db)):
    return department.create_department(db=db, obj_in=departments)


@department_router.get("/", response_model=List[Department])
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return department.get_multi_department(db, skip=skip, limit=limit)


# is it neccessary to create a schema for user_department
@department_router.post("/{dept_id}", response_model=UserDepartment)
def assign_department(user_id: UUID, dept_id: int, db: Session = Depends(get_db)):
    db_user = user.get_user_id(db, id=user_id)
    db_dept = department.get_dept_id(db, id=dept_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return userdept.assign_department(user_id=user_id, dept_id=dept_id, db=db)
    # TODO avoid repeating the same entry


@department_router.get("/{user_id}/departments/{dept_id}")
def get_user_departments(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return userdept.get_user_department(db, skip=skip, limit=limit)
