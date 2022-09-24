from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.crud.msg import CRUDMessage
from ...app.models.users import Users
from ...app.schemas.notification import NotificationCreate, NotificationUpdate


class CRUDNotification(CRUDBase[Users, NotificationCreate, NotificationUpdate]):
    def send_notification(from_user: int, db: Session, to_user=int):
        admin = (
            db.query(Users.is_admin)
            .filter(Users.user_id == from_user)
            .filter(Users.is_admin == "true")
            .first()
        )
        # if not user:
        #     raise HTTPException(status_code=)
        if admin:
            return CRUDMessage.assign_message(user_id=to_user, db=db)
        else:
            return "User doesn't have enough Priviledges"


notification = CRUDNotification(Users)
