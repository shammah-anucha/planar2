from fastapi import APIRouter, Depends
from . import schema, crud
from ....app.modules.common.db.session import get_db
from typing import List
from sqlalchemy.orm import Session
from ....app.modules.events.model import Event
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
