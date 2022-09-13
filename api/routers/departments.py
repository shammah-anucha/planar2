from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..dependencies import get_db
from sqlalchemy.orm import Session
from api import crud, schemas

router = APIRouter(
    prefix="/departments", tags=["departments"], dependencies=[Depends(get_db)]
)

# departments
@router.post("/", response_model=schemas.Department)
def create_department(
    department: schemas.DepartmentCreate, db: Session = Depends(get_db)
):
    return crud.create_department(db=db, department=department)


@router.get("/user/", response_model=List[schemas.Department])
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_department(db, skip=skip, limit=limit)


# is it neccessary to create a schema for user_department
@router.post("/{user_id}/{dept_id}")
def assign_department(user_id: int, dept_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_id(db, id=user_id)
    db_dept = crud.get_dept_id(db, id=dept_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.assign_department(user_id=user_id, dept_id=dept_id, db=db)
    # TODO avoid repeating the same entry


@router.get("/")
def get_user_departments(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_user_department(db, skip=skip, limit=limit)
