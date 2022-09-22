from typing import Any, List
from pydantic import EmailStr

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.models.users import User


class CRUDEmail(CRUDBase[User]):
    def get_available_emails(self, db: Session) -> List[User.email]:
        emails = []
        for email in db.query(User.email).filter(User.unavailabilities == None).all():
            email = "\n".join(list(email))
            emails.append(email)
        return emails


crud_email = CRUDEmail(User)
