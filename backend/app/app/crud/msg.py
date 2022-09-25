from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.models.msg import Messages
from ...app.schemas.msg import MessageCreate, MessageUpdate


def assign_message(db: Session, user_id: int):
    message = "You have been invited to serve"
    db_message = Messages(user_id=user_id, message=message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
