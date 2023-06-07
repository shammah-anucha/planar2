from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from ....app.modules.common.utils.core.security import (
    get_password_hash,
    verify_password,
)
from ...modules.common.utils.base import CRUDBase
from ...modules.users.model import Users
from ...modules.users.schema import UserCreate, UserUpdate
from ...modules.common.utils.country_code import CountryCodes


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    def get_user_by_email(self, db: Session, email: str) -> Optional[Users]:
        return db.query(Users).filter(Users.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> Users:
        # Max phone digits: https://en.wikipedia.org/wiki/Telephone_numbering_plan#:~:text=It%20is%20an%20open%20numbering,number%20for%20international%20destination%20routing.
        db_user = Users(
            email=obj_in.email,
            firstname=obj_in.firstname,
            lastname=obj_in.lastname,
            dob=obj_in.dob,
            # nationality=obj_in.nationality,
            # country_of_residence=obj_in.country_of_residence,
            phone=obj_in.phone,
            # country_code=obj_in.country_code.value,
            is_admin=obj_in.is_admin,
            hashed_password=get_password_hash(obj_in.password),
        )
        phone_length = len(str(db_user.phone))
        if not (phone_length >= 7 and phone_length <= 11):
            raise HTTPException(
                status_code=502,
                detail="Invalid Phone Number",
            )
        # db_user.phone = str(db_user.country_code) + str(db_user.phone)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(
        self, db: Session, *, db_obj: Users, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> Users:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi_user(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Users]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_user_id(self, db: Session, id: Any):
        return db.query(Users).filter(Users.user_id == id).first()

    def authenticate_user(
        self, db: Session, *, email: str, password: str
    ) -> Optional[Users]:
        user = self.get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def disabled(self, user: Users) -> bool:
        return user.disabled

    def is_admin(self, user: Users) -> bool:
        return user.is_admin

    # def is_admin(self, sender_id: int, db: Session) -> bool:

    #     admin = (
    #         db.query(Users.is_admin)
    #         .filter(Users.user_id == sender_id)
    #         .filter(Users.is_admin == "true")
    #         .first()
    #     )
    #     if admin:
    #         return Users.is_admin
    #     else:
    #         return "User does not have enough privileges"


user = CRUDUser(Users)
