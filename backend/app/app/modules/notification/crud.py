from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import null, select, update

from ....app.modules.common.utils.base import CRUDBase
from ....app.modules.messages.crud import assign_message
from ....app.modules.users.model import Users
from ....app.modules.roster.model import Roster
from ....app.modules.roster.schema import Response
from ....app.modules.messages.model import Messages
from ....app.modules.messages.schema import MessageForm
from ....app.modules.notification.schema import NotificationCreate, NotificationUpdate


def insert_message(db: Session, msg: str):
    pass


def send_all_notification(db: Session):
    # check responses in roster model that are none
    # response = db.query(Roster.response).filter.all()
    # user_id_in_msg = db.query(Messages.user_id).all()
    # user_id_in_roster = db.query(Roster.user_id).all()

    # response_date = db.query(Roster.response_date).first()

    # inbox = (
    #     update(Messages)
    #     .where(Roster.response is null)
    #     .where(Roster.user_id is not null)
    #     .values(message="You have been invited to serve")
    # )
    # db.add(inbox)
    # db.commit()
    # db.refresh(inbox)
    inbox = (
        update(Messages)
        .where(Roster.response is null)
        .where(Roster.user_id is not null)
        .values(message="You have been invited to serve")
    )
    db.add(inbox)
    db.commit()
    db.refresh(inbox)
    # for id in user_id_in_roster:
    #     Messages.user_id = id
    #     db.add(Messages.user_id)
    #     db.commit()
    #     db.refresh(Messages.user_id)

    # for id in user_id:
    #     if response is None:
    #         reply = MessageFormat.invitation
    #         inbox = Messages(message=reply, user_id=id)
    #         db.add(inbox)
    #         db.commit()
    #         db.refresh(inbox)
    #         return inbox


# notification types: request volunteer, reminder,

# def get_email_in_department(self, dept_id: int, db: Session) -> List[EmailStr]:
#     emails = []
#     for email, dept_id in (
#         db.query(Users.email, UserDepartment.dept_id)
#         .filter(Users.user_id == UserDepartment.user_id)
#         .filter(UserDepartment.dept_id == dept_id)
#         .all()
#     ):
#         email = "".join(list(email))
#         emails.append(email)
#     return emails
