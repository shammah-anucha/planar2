from typing import Any, List
from pydantic import EmailStr

from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.users.model import Users
from ...modules.userdepartment.model import UserDepartment
from ...modules.userdepartment.schema import UserDepartmentCreate, UserDepartmentUpdate


class CRUDUserDepartment(
    CRUDBase[UserDepartment, UserDepartmentCreate, UserDepartmentUpdate]
):
    def assign_department(
        self,
        db: Session,
        *,
        dept_id: UserDepartmentCreate,
        user_id: UserDepartmentCreate
    ) -> UserDepartment:
        db_obj = self.model(user_id=user_id, dept_id=dept_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_user_department(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[UserDepartment]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_email_in_department(self, dept_id: int, db: Session) -> List[EmailStr]:
        emails = []
        for email, dept_id in (
            db.query(Users.email, UserDepartment.dept_id)
            .filter(Users.user_id == UserDepartment.user_id)
            .filter(UserDepartment.dept_id == dept_id)
            .all()
        ):
            email = "".join(list(email))
            emails.append(email)
        return emails


userdept = CRUDUserDepartment(UserDepartment)
