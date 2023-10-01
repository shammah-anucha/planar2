import re
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from . import crud, model
from ....app.modules.common.db.session import get_db
from ....app.modules.users.crud import user
from ....app.modules.users import utils
from sqlalchemy.orm import Session
from ...modules.roster_short.schema import RosterShortInDB


from ...modules.roster.crud import roster
from uuid import UUID


rostershort_router = APIRouter(
    prefix="/rostershort", tags=["rostershort"], dependencies=[Depends(get_db)]
)


@rostershort_router.get("/", response_model=List[RosterShortInDB])
def read_roster(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_roster_short(db, skip=skip, limit=limit)


@rostershort_router.get("/{user_id}", response_model=List[RosterShortInDB])
def read_user_roster(user_id: UUID, db: Session = Depends(get_db)):
    return crud.read_user_roster_short(user_id=user_id, db=db)


@rostershort_router.get("/accepted/{user_id}", response_model=List[RosterShortInDB])
def read_accepted_user_roster(user_id: UUID, db: Session = Depends(get_db)):
    return crud.read_accepted_user_roster_short(user_id=user_id, db=db)
