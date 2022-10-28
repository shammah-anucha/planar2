import re
from typing import List, Optional
from fastapi import Depends
from ....app.modules.common.db.session import get_db

from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.users.model import Users
from ...modules.roster.model import Roster

# from ...modules.responses.schema import Responses
from ...modules.responses.model import Responses
from ...modules.roster.schema import RosterCreate, RosterUpdate


class CRUDRoster(CRUDBase[Roster, RosterCreate, RosterUpdate]):
    def create_roster(self, db: Session, *, event_id: int, user_id: int) -> Roster:
        response = str(
            db.query(Responses.response).filter(Responses.user_id == user_id).all()
        )
        if response == "Accept":
            Firstname = str(
                db.query(Users.Firstname).filter(Users.user_id == user_id).all()
            )

            Lastname = str(
                db.query(Users.Lastname).filter(Users.user_id == user_id).all()
            )
            Firstname = (re.search(r"(\w+)", Firstname)).group(0)
            Lastname = (re.search(r"(\w+)", Lastname)).group(0)

            db_obj = self.model(
                user_id=user_id,
                event_id=event_id,
                Firstname=Firstname,
                Lastname=Lastname,
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj

    def read_roster(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Users]:
        return db.query(self.model).offset(skip).limit(limit).all()


roster = CRUDRoster(Roster)
