from typing import Any, List
from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.userroleassigned.model import UserRolesAssigned
from ...modules.userroleassigned.schema import (
    UserRoleAssignedCreate,
    UserRoleAssignedUpdate,
)
from ....app.modules.users.crud import user
from ....app.modules.userrole.crud import userroles

from ...modules.users.model import Users
from uuid import UUID
import re


class CRUDUserRolesAssigned(
    CRUDBase[UserRolesAssigned, UserRoleAssignedCreate, UserRoleAssignedUpdate]
):
    def assign_userrole(self, user_id: UUID, userrole_id: int, db: Session):
        db_user = user.get_user_id(db, id=user_id)
        db_role = userroles.get_userrole_id(db, id=userrole_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if db_role is None:
            raise HTTPException(status_code=404, detail="UserRole not found")

        Firstname = str(
            db.query(Users.Firstname).filter(Users.user_id == user_id).all()
        )

        Lastname = str(db.query(Users.Lastname).filter(Users.user_id == user_id).all())
        Firstname = (re.search(r"(\w+)", Firstname)).group(0)
        Lastname = (re.search(r"(\w+)", Lastname)).group(0)

        db_obj = self.model(
            user_id=user_id,
            userrole_id=userrole_id,
            Firstname=Firstname,
            Lastname=Lastname,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_userrolesassigned(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[UserRolesAssigned]:
        return db.query(self.model).offset(skip).limit(limit).all()


userrolesassigned = CRUDUserRolesAssigned(UserRolesAssigned)
