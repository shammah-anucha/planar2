from typing import Any, Dict, Optional, Union, List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, status
from ....app.modules.common.db.session import get_db
from uuid import UUID


from ...modules.common.utils.base import CRUDBase
from ...modules.events.model import Event
from ...modules.events.schema import EventCreate, EventUpdate, Volunteer
from pydantic import BaseModel, HttpUrl
from ...modules.users.model import Users
from ...modules.common.db.session import engine


class CRUDEvent(CRUDBase[Event, EventCreate, EventUpdate]):
    def create_event(self, db: Session, *, obj_in: EventCreate) -> Event:
        db_user = Event(
            title=obj_in.title,
            location=obj_in.location,
            location_url=obj_in.location_url,
            eventdate=obj_in.eventdate,
            time=obj_in.time,
            imageUrl=obj_in.imageUrl,
            host=obj_in.host,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    # def create_event(self, db: Session, *, obj_in: EventCreate) -> Event:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def get_multi_events(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Event]:
        return db.query(self.model).offset(skip).limit(limit).all()

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

    def update_event(
        self, event_id: UUID, *, response: EventUpdate, db: Session = Depends(get_db)
    ) -> Event:
        # if isinstance(obj_in, dict):
        #     update_data = obj_in
        # else:
        #     update_data = obj_in.dict(exclude_unset=True)

        event_query = db.query(Event).filter(Event.event_id == event_id)
        db_event = event_query.first()
        if not db_event:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail=f"No event with this id: {event_id} found",
            )
        event_query.update(response.dict(exclude_none=True), synchronize_session=False)
        db.commit()
        return db_event


event = CRUDEvent(Event)


# with Session(engine) as session:
#     volunteer = session.query(Users).filter(Users.user_id == user_id)
#     event = session.query(Event).filter(Event.event_id == event_id)
#     association = volunteer.assigned_events.append(volunteer)

#     # with Session(engine) as session:
#     #     volunteer = session.exec(select(Users).where(Users.user_id == user_id)).one()
#     db.add(association)
#     db.commit()
#     db.refresh(association)
#     return association


# def update_heroes():
#     with Session(engine) as session:
#         hero_spider_boy = session.exec(
#             select(Hero).where(Hero.name == "Spider-Boy")
#         ).one()
#         team_z_force = session.exec(select(Team).where(Team.name == "Z-Force")).one()

#         team_z_force.heroes.append(hero_spider_boy)
#         session.add(team_z_force)
#         session.commit()

#         print("Updated Spider-Boy's Teams:", hero_spider_boy.teams)
#         print("Z-Force heroes:", team_z_force.heroes)
