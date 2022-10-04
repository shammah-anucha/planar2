from typing import Any, List
from pydantic import EmailStr

from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.models import models
from ...app.schemas.userdept import UserDepartmentCreate, UserDepartmentUpdate


class CRUDUserDepartment(
    CRUDBase[models.UserDepartment, UserDepartmentCreate, UserDepartmentUpdate]
):
    def assign_department(
        self,
        db: Session,
        *,
        dept_id: UserDepartmentCreate,
        user_id: UserDepartmentCreate
    ) -> models.UserDepartment:
        db_obj = self.model(user_id=user_id, dept_id=dept_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_user_department(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[models.UserDepartment]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_email_in_department(self, dept_id: int, db: Session) -> List[EmailStr]:
        emails = []
        for email, dept_id in (
            db.query(models.Users.email, models.UserDepartment.dept_id)
            .filter(models.Users.user_id == models.UserDepartment.user_id)
            .filter(models.UserDepartment.dept_id == dept_id)
            .all()
        ):
            email = "".join(list(email))
            emails.append(email)
        return emails


userdept = CRUDUserDepartment(models.UserDepartment)
