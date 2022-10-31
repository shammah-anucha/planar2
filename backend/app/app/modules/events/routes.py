from fastapi import APIRouter, Depends
from . import schema, crud
from fastapi.encoders import jsonable_encoder
from ....app.modules.common.db.session import get_db
from typing import List
from sqlalchemy.orm import Session
from ....app.modules.events.model import Event
from ...modules.roster.schema import Roster, RosterCreate

# from ...modules.roster.crud import roster
from datetime import date


event_router = APIRouter(
    prefix="/events", tags=["events"], dependencies=[Depends(get_db)]
)

# works
@event_router.post("/", response_model=schema.Event)
def create_event(event: schema.EventCreate, db: Session = Depends(get_db)):
    return crud.event.create_event(db=db, obj_in=event)


# works
@event_router.get("/", response_model=List[schema.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.event.get_multi_events(db, skip=skip, limit=limit)


# works
@event_router.get("/upcoming_events")
def read_upcoming_events(db: Session = Depends(get_db)):
    return db.query(Event).filter(Event.date >= date.today()).all()


# not working
@event_router.put("/", response_model=schema.Volunteer)
def assign_volunteer(volunteer: schema.Volunteer, db: Session = Depends(get_db)):
    return crud.event.assign_event(db=db, obj_in=volunteer)


# @router.put("/me", response_model=schemas.User)
# def update_user_me(
#     *,
#     db: Session = Depends(deps.get_db),
#     password: str = Body(None),
#     full_name: str = Body(None),
#     email: EmailStr = Body(None),
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update own user.
#     """
#     current_user_data = jsonable_encoder(current_user)
#     user_in = schemas.UserUpdate(**current_user_data)
#     if password is not None:
#         user_in.password = password
#     if full_name is not None:
#         user_in.full_name = full_name
#     if email is not None:
#         user_in.email = email
#     user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
#     return user
