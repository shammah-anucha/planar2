from fastapi import APIRouter, Depends
from uuid import UUID
from . import schema, model, crud
from fastapi.encoders import jsonable_encoder
from ....app.modules.common.db.session import get_db
from typing import List, Optional
from sqlalchemy.orm import Session

# from ....app.modules.events.model import Event
# from ....app.modules.events.schema import Event
from ...modules.roster.schema import Roster, RosterCreate
from pydantic import BaseModel, HttpUrl

# from ...modules.roster.crud import roster
from datetime import date


event_router = APIRouter(
    prefix="/events", tags=["events"], dependencies=[Depends(get_db)]
)


# works
@event_router.post("/{event_id}", response_model=schema.Event)
def create_event(*, event_in: schema.EventCreate, db: Session = Depends(get_db)):
    return crud.event.create_event(db=db, obj_in=event_in)


# works
@event_router.get("/", response_model=List[schema.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.event.get_multi_events(db, skip=skip, limit=limit)


# works
@event_router.get("/upcoming_events")
def read_upcoming_events(db: Session = Depends(get_db)):
    return db.query(model.Event).filter(model.Event.date >= date.today()).all()


@event_router.put("/{event_id}", response_model=schema.Event)
def update_event(
    event_id: UUID,
    response: schema.EventUpdate,
    # event_id: UUID,
    db: Session = Depends(get_db),
):
    return crud.event.update_event(
        db=db,
        event_id=event_id,
        response=response,
    )


@event_router.delete("/{event_id}")
def delete_event(event_id: UUID, db: Session = Depends(get_db)):
    db.query(model.Event).filter(model.Event.event_id == event_id).delete()
    db.commit()
    return f"Event Deleted!"
