from fastapi import APIRouter, HTTPException, Depends
from typing import Any, List
from sqlalchemy.orm import Session
from .....app.schemas.users import User, UserCreate
from .....app.models.users import Users
from .....app.api import deps
from ....crud import crud_user


router = APIRouter()


@router.post("/users/", response_model=User, tags=["users"])
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)) -> Any:
    """Create new user."""
    db_user = crud_user.user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.user.create_user(db=db, user=db_user)


# works
@router.get("/users/", response_model=List[User], tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    users = crud_user.user.get_multi_user(db, skip=skip, limit=limit)
    return users


# works
@router.get("/users/{user_id}", response_model=User, tags=["users"])
def read_user(user_id: int, db: Session = Depends(deps.get_db)):
    db_user = crud_user.user.get_user_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: int, db: Session = Depends(deps.get_db)):
    db.query(Users).filter(Users.user_id == user_id).delete()
    db.commit()
    return "Delete Successful"
