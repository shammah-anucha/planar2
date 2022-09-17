from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create_user(db: Session, user: UserCreate) -> Optional[User]:
        db_user = User(
            email=user.email,
            username=user.username,
            Firstname=user.Firstname,
            Lastname=user.Lastname,
            D_O_B=user.D_O_B,
            country_of_residence=user.country_of_residence,
            phone=user.phone,
            is_admin=user.is_admin,
            hashed_password=get_password_hash(user.password),
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate_user(
        self, db: Session, email: str, password: str
    ) -> Optional[User]:
        user = self.get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def disabled(self, user: User) -> bool:
        return user.disabled

    def is_admin(self, user: User) -> bool:
        return user.is_admin


user = CRUDUser(User)
