import re
from datetime import datetime
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from uuid import UUID

from . import schema
from backend.app.app.modules.messages.crud import assign_message

from ....app.modules.common.db.session import get_db

from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.users.model import Users
from ...modules.events.model import Event
from ...modules.users.crud import user
from ...modules.roster_short.crud import create_roster_short
from ...modules.users.utils import get_admin
from ...modules.roster.model import Roster
from ...modules.userrole.model import UserRoles


from . import schema


class CRUDRoster(CRUDBase[Roster, schema.RosterCreate, schema.RosterUpdate]):
    def get_volunteer(
        self, db: Session, user_id: UUID, event_id: UUID, userrole_id: int
    ) -> Optional[Roster]:
        return (
            db.query(Roster)
            .filter(Roster.user_id == user_id)
            .filter(Roster.event_id == event_id)
            .filter(Roster.userrole_id == userrole_id)
            .first()
        )

    def get_volunteer_response(
        self, db: Session, roster_id: int, response: str
    ) -> Optional[Roster]:
        return (
            db.query(Roster)
            .filter(Roster.roster_id == roster_id)
            .filter(Roster.response == response)
            .first()
        )

    def create_roster(
        self,
        db: Session,
        *,
        sender_id: UUID,
        user_id: UUID,
        event_id: UUID,
        userrole_id: int,
    ) -> Roster:
        volunteer = roster.get_volunteer(
            db=db, user_id=user_id, event_id=event_id, userrole_id=userrole_id
        )
        admin = (
            db.query(Users.is_admin)
            .filter(Users.user_id == sender_id)
            .filter(Users.is_admin == "true")
            .first()
        )

        Firstname = str(
            db.query(Users.firstname).filter(Users.user_id == user_id).all()
        )

        Lastname = str(db.query(Users.lastname).filter(Users.user_id == user_id).all())
        userrole = str(
            db.query(UserRoles.role).filter(UserRoles.userrole_id == userrole_id).all()
        )
        title = str(db.query(Event.title).filter(Event.event_id == event_id).first())
        event_date = str(
            db.query(Event.eventdate).filter(Event.event_id == event_id).first()
        )
        time = str(db.query(Event.time).filter(Event.event_id == event_id).first())
        Firstname = (re.search(r"(\w+)", Firstname)).group(0)
        Lastname = (re.search(r"(\w+)", Lastname)).group(0)
        userrole = (re.search(r"(\w+\ *\w*)", userrole)).group(0)
        title = (re.search(r"(\w+\ *\w*)", title)).group(0)
        event_date = (re.search(r"(\w{4}-\w{2}-\w{2})", event_date)).group(0)
        time = (re.search(r"(\w+\ *\w*)", time)).group(0)

        db_obj = self.model(
            sender_id=sender_id,
            user_id=user_id,
            event_id=event_id,
            userrole_id=userrole_id,
            Firstname=Firstname,
            Lastname=Lastname,
            role=userrole,
            created_at=datetime.utcnow(),
        )

        if not admin:
            raise HTTPException(
                status_code=404,
                detail="User does not have enough privileges",
            )

        if volunteer:
            raise HTTPException(
                status_code=400, detail="Volunteer Already Assigned to Event"
            )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        create_roster_short(
            title=title,
            role=userrole,
            event_date=event_date,
            time=time,
            user_id=user_id,
            db=db,
            roster_id=db_obj.roster_id,
        )
        # assign_message(user_id=user_id, db=db)
        return db_obj

    def read_roster(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Roster]:
        return db.query(self.model).offset(skip).limit(limit).all()

    # inspired from: https://codevoweb.com/crud-restful-api-server-with-python-fastapi-and-postgresql/
    def volunteer_response(
        self,
        roster_id: int,
        *,
        response: schema.RosterUpdate,
        db: Session = Depends(get_db),
    ) -> Roster:
        roster_query = db.query(Roster).filter(Roster.roster_id == roster_id)
        db_roster = roster_query.first()
        if not db_roster:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail=f"No roster with this id: {roster_id} found",
            )
        roster_query.update(response.dict(exclude_none=True), synchronize_session=False)
        db.commit()
        return db_roster

    # def update_event(
    #     self, event_id: UUID, *, response: EventUpdate, db: Session = Depends(get_db)
    # ) -> Event:
    #     # if isinstance(obj_in, dict):
    #     #     update_data = obj_in
    #     # else:
    #     #     update_data = obj_in.dict(exclude_unset=True)

    #     event_query = db.query(Event).filter(Event.event_id == event_id)
    #     db_event = event_query.first()
    #     if not db_event:
    #         raise HTTPException(
    #             status_code=status.HTTP_200_OK,
    #             detail=f"No event with this id: {event_id} found",
    #         )
    #     event_query.update(response.dict(exclude_none=True), synchronize_session=False)
    #     db.commit()
    #     return db_event

    # def volunteer_response(
    #     self,
    #     roster_id: int,
    #     response: schema.RosterUpdate,
    #     user_id: UUID,
    #     db: Session = Depends(get_db),
    # ) -> Roster:
    #     roster_query = db.query(Roster).filter(Roster.roster_id == roster_id)
    #     db_roster = roster_query.first()
    #     if not db_roster:
    #         raise HTTPException(
    #             status_code=status.HTTP_200_OK,
    #             detail=f"No roster with this id: {roster_id} found",
    #         )

    #     volunteer = user.get_user_id(db, id=user_id)
    #     if not volunteer:
    #         raise HTTPException(
    #             status_code=404,
    #             detail="The user with this username does not exist in the system",
    #         )
    #     # just for testing purposes, in the real sense it's supposed to only show two options, Accept or Decline and accessed by clicking
    #     if not (
    #         str(response.response) == schema.Response.Accept.value
    #         or str(response.response) == schema.Response.Decline.value
    #     ):
    #         raise HTTPException(
    #             status_code=502,
    #             detail="Invalid Response",
    #         )

    #     response.response_date = datetime.utcnow()
    #     roster_query.update(response.dict(exclude_none=True), synchronize_session=False)
    #     db.commit()
    #     return db_roster


roster = CRUDRoster(Roster)
