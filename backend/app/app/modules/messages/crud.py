from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.messages.model import Messages
from ...modules.messages.schema import MessageCreate, MessageUpdate


def assign_message(db: Session, user_id: int):
    message = "You have been invited to serve"
    db_message = Messages(user_id=user_id, message=message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def check_inbox(db: Session, user_id: int):
    return db.query(Messages).filter(Messages.user_id == user_id).first()
