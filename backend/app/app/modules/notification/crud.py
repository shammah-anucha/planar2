from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ....app.modules.common.utils.base import CRUDBase
from ....app.modules.messages.crud import assign_message
from ....app.modules.users.model import Users
from ....app.modules.notification.schema import NotificationCreate, NotificationUpdate


# transferred
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
        return assign_message(user_id=to_user, db=db)
    else:
        return "User doesn't have enough Priviledges"
