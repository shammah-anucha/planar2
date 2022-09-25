from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from ...app.core.security import get_password_hash, verify_password
from ...app.crud.base import CRUDBase
from ...app.models.users import Users
from ...app.schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    def get_user_by_email(self, db: Session, email: str) -> Optional[Users]:
        return db.query(Users).filter(Users.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> Users:
        db_user = Users(
            email=obj_in.email,
            username=obj_in.username,
            Firstname=obj_in.Firstname,
            Lastname=obj_in.Lastname,
            D_O_B=obj_in.D_O_B,
            country_of_residence=obj_in.country_of_residence,
            phone=obj_in.phone,
            is_admin=obj_in.is_admin,
            hashed_password=get_password_hash(obj_in.password),
        )
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


user = CRUDUser(Users)
