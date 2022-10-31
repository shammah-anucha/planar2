import re
from datetime import date, datetime
from typing import List, Optional, Union, Dict, Any
from fastapi import Depends, HTTPException, status
from ....app.modules.common.db.session import get_db

from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.users.model import Users
from ...modules.roster.model import Roster

from . import schema
from ....app.modules.users.crud import user


class CRUDRoster(CRUDBase[Roster, schema.RosterCreate, schema.RosterUpdate]):
    def create_roster(
        self, db: Session, *, sender_id: int, user_id: int, event_id: int
    ) -> Roster:
        Firstname = str(
            db.query(Users.Firstname).filter(Users.user_id == user_id).all()
        )

        Lastname = str(db.query(Users.Lastname).filter(Users.user_id == user_id).all())
        Firstname = (re.search(r"(\w+)", Firstname)).group(0)
        Lastname = (re.search(r"(\w+)", Lastname)).group(0)

        db_obj = self.model(
            sender_id=sender_id,
            user_id=user_id,
            event_id=event_id,
            Firstname=Firstname,
            Lastname=Lastname,
            created_at=datetime.utcnow(),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def read_roster(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Roster]:
        return db.query(self.model).offset(skip).limit(limit).all()

    # inspired from: https://codevoweb.com/crud-restful-api-server-with-python-fastapi-and-postgresql/
    def volunteer_response(
        self,
        roster_id: int,
        response: schema.RosterUpdate,
        user_id: int,
        db: Session = Depends(get_db),
    ) -> Roster:
        roster_query = db.query(Roster).filter(Roster.roster_id == roster_id)
        db_roster = roster_query.first()
        if not db_roster:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail=f"No post with this id: {roster_id} found",
            )

        volunteer = user.get_user_id(db, id=user_id)
        if not volunteer:
            raise HTTPException(
                status_code=404,
                detail="The user with this username does not exist in the system",
            )
        response.response_date = datetime.utcnow()
        roster_query.update(response.dict(exclude_none=True), synchronize_session=False)
        db.commit()
        return db_roster


roster = CRUDRoster(Roster)
