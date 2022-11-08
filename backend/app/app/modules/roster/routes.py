import re
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from . import crud, model
from ....app.modules.common.db.session import get_db
from ....app.modules.users.crud import user
from sqlalchemy.orm import Session
from ...modules.roster.schema import Roster, RosterUpdate, RosterInDB

from ...modules.roster.crud import roster
from uuid import UUID


roster_router = APIRouter(
    prefix="/roster", tags=["roster"], dependencies=[Depends(get_db)]
)


@roster_router.post("/", response_model=Roster)
def create_roster(
    userid: UUID,
    eventid: int,
    sender_id: int,
    db: Session = Depends(get_db),
):

    return roster.create_roster(
        db=db, sender_id=sender_id, event_id=eventid, user_id=userid
    )


@roster_router.put("/", response_model=Roster)
def volunteer_response(
    response: RosterUpdate,
    roster_id: int,
    user_id: UUID,
    db: Session = Depends(get_db),
):
    return roster.volunteer_response(
        db=db, response=response, roster_id=roster_id, user_id=user_id
    )


@roster_router.get("/", response_model=List[RosterInDB])
def read_roster(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.roster.read_roster(db, skip=skip, limit=limit)


@roster_router.delete("/{roster_id}")
def remove_assignee(rosterid: int, db: Session = Depends(get_db)):
    Firstname = str(
        db.query(model.Roster.Firstname)
        .filter(model.Roster.roster_id == rosterid)
        .all()
    )
    Firstname = (re.search(r"(\w+)", Firstname)).group(0)
    db.query(model.Roster).filter(model.Roster.roster_id == rosterid).delete()
    db.commit()
    return f"Unassigned {Firstname} from event!"
