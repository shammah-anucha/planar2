from typing import Any, List
from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.userrole.model import UserRoles
from ...modules.userrole.schema import UserRoleCreate, UserRoleUpdate
from ....app.modules.users.crud import user


class CRUDUserRoles(CRUDBase[UserRoles, UserRoleCreate, UserRoleUpdate]):
    def create_userrole(self, db: Session, *, obj_in: UserRoleCreate) -> UserRoles:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_userroles(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[UserRoles]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_userrole_id(self, db: Session, id: Any) -> List[UserRoles]:
        return (
            db.query(UserRoles.userrole_id).filter(UserRoles.userrole_id == id).first()
        )


userroles = CRUDUserRoles(UserRoles)
