from fastapi import APIRouter, HTTPException, Depends
from typing import List
from .....app.api import deps
from sqlalchemy.orm import Session
from ....schemas.departments import Department, DepartmentCreate
from ....schemas.userdept import UserDepartment
from .....app.crud import crud_user, departments, userdept

router = APIRouter(
    prefix="/departments", tags=["departments"], dependencies=[Depends(deps.get_db)]
)

# departments
@router.post("/", response_model=Department)
def create_department(department: DepartmentCreate, db: Session = Depends(deps.get_db)):
    return departments.department.create_department(db=db, obj_in=department)


@router.get("/user/", response_model=List[Department])
def get_departments(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    return departments.department.get_multi_department(db, skip=skip, limit=limit)


# is it neccessary to create a schema for user_department
@router.post("/{user_id}/{dept_id}", response_model=UserDepartment)
def assign_department(user_id: int, dept_id: int, db: Session = Depends(deps.get_db)):
    db_user = crud_user.user.get_user_id(db, id=user_id)
    db_dept = departments.department.get_dept_id(db, id=dept_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return userdept.userdept.assign_department(user_id=user_id, dept_id=dept_id, db=db)
    # TODO avoid repeating the same entry


@router.get("/")
def get_user_departments(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    return userdept.userdept.get_user_department(db, skip=skip, limit=limit)
