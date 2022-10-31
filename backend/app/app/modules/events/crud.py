from typing import Any, Dict, Optional, Union, List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.events.model import Event
from ...modules.events.schema import EventCreate, EventUpdate, Volunteer
from ...modules.users.model import Users
from ...modules.common.db.session import engine


class CRUDEvent(CRUDBase[Event, EventCreate, EventUpdate]):
    def create_event(self, db: Session, *, obj_in: EventCreate) -> Event:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_events(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Event]:
        return db.query(self.model).offset(skip).limit(limit).all()

    # def assign_event(
    #     self, db: Session, *, db_obj: Event, obj_in: Union[EventUpdate, Dict[str, Any]]
    # ) -> Event:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)


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
