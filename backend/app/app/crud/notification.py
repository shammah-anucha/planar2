from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.crud.msg import CRUDMessage
from ...app.models.users import User
from ...app.schemas.notification import NotificationCreate


class CRUDNotification(CRUDBase[User, NotificationCreate]):
    def send_notification(from_user: int, db: Session, to_user=int):
        admin = (
            db.query(User.is_admin)
            .filter(User.user_id == from_user)
            .filter(User.is_admin == "true")
            .first()
        )
        # if not user:
        #     raise HTTPException(status_code=)
        if admin:
            return CRUDMessage.assign_message(user_id=to_user, db=db)
        else:
            return "User doesn't have enough Priviledges"


notification = CRUDNotification(User)
