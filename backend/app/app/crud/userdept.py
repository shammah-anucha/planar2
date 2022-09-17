from typing import Any, List
from pydantic import EmailStr

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.departments import UserDepartment
from app.models.users import User
from app.schemas.userdept import UserDepartmentCreate


class CRUDUserDepartment(CRUDBase[UserDepartmentCreate, UserDepartment]):
    def assign_department(
        self, db: Session, *, obj_in: UserDepartmentCreate
    ) -> UserDepartment:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
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
            db.query(User.email, UserDepartment.dept_id)
            .filter(User.user_id == UserDepartment.user_id)
            .filter(UserDepartment.dept_id == dept_id)
            .all()
        ):
            email = "".join(list(email))
            emails.append(email)
        return emails


userdept = CRUDUserDepartment(UserDepartment)
