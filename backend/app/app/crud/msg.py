from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.models.msg import Messages
from ...app.schemas.msg import MessageCreate


class CRUDMessage(CRUDBase[Messages, MessageCreate]):
    def assign_message(self, db: Session, *, obj_in: MessageCreate):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


message = CRUDMessage(Messages)
