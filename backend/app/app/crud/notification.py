from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.crud.msg import assign_message
from ...app.models import models
from ...app.schemas.notification import NotificationCreate, NotificationUpdate


# transferred
def send_notification(from_user: int, db: Session, to_user=int):
    admin = (
        db.query(models.Users.is_admin)
        .filter(models.Users.user_id == from_user)
        .filter(models.Users.is_admin == "true")
        .first()
    )
    # if not user:
    #     raise HTTPException(status_code=)
    if admin:
        return assign_message(user_id=to_user, db=db)
    else:
        return "User doesn't have enough Priviledges"
