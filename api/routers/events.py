from fastapi import APIRouter, Depends, HTTPException
from api import crud, schemas
from ..dependencies import get_db
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(prefix="/events", tags=["events"], dependencies=[Depends(get_db)])

# works
@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)


# works
@router.get("/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roster = crud.get_events(db, skip=skip, limit=limit)
    return roster
