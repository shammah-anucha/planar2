from fastapi import APIRouter, Depends
from ....crud import crud_events
from ....schemas import events
from .....app.api import deps
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/events", tags=["events"], dependencies=[Depends(deps.get_db)]
)

# works
@router.post("/", response_model=events.Event)
def create_event(event: events.EventCreate, db: Session = Depends(deps.get_db)):
    return crud_events.event.create_event(db=db, obj_in=event)


# works
@router.get("/", response_model=List[events.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    roster = crud_events.event.get_multi_events(db, skip=skip, limit=limit)
    return roster
