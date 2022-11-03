from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import model, crud, schema
from ....app.modules.common.db.session import get_db


notification_router = APIRouter()


@notification_router.get(
    "/users/{user_id}/notification", response_model=schema.Message, tags=["users"]
)
def read_notification(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.check_inbox(db, user_id=user_id)
    # if db_user is None:
    #     raise HTTPException(status_code=404, detail="User not found")
    return db_user
