from fastapi import APIRouter, HTTPException, Depends
from typing import Any, List
from sqlalchemy.orm import Session
from .schema import User, UserCreate
from . import model, utils, crud
from ....app.modules.common.db.session import get_db

# from ....app.modules.notification.crud import send_notification


user_router = APIRouter()

# works
@user_router.post("/users/", response_model=User, tags=["users"])
def create_user(*, users_in: UserCreate, db: Session = Depends(utils.get_db)) -> Any:
    """Create new user."""
    user = crud.user.get_user_by_email(db, email=users_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create(db=db, obj_in=users_in)


# works
@user_router.get("/users/", response_model=List[User], tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(utils.get_db)):
    users = crud.user.get_multi_user(db, skip=skip, limit=limit)
    return users


# works
@user_router.get("/users/{user_id}", response_model=User, tags=["users"])
def read_user(user_id: int, db: Session = Depends(utils.get_db)):
    db_user = crud.user.get_user_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: int, db: Session = Depends(utils.get_db)):
    db.query(model.Users).filter(model.Users.user_id == user_id).delete()
    db.commit()
    return "Delete Successful"


# @user_router.get("/users/{user_id}/notification/{from_user}/{to_user}", tags=["users"])
# def notification(
#     from_user: int,
#     to_user: int,
#     db: Session = Depends(get_db),
# ):
#     return send_notification(from_user=from_user, db=db, to_user=to_user)
