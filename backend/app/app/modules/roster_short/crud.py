from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from ...modules.roster_short.model import RosterShort
from ...modules.roster.model import Roster
from uuid import UUID
from ....app.modules.users.crud import user
from ....app.modules.users import utils
from fastapi import APIRouter, HTTPException, Depends, status


def create_roster_short(
    title: str,
    role: str,
    event_date: str,
    time: str,
    user_id: UUID,
    roster_id: int,
    db: Session,
):
    db_roster_short = RosterShort(
        title=title,
        role=role,
        event_date=event_date,
        time=time,
        user_id=user_id,
        roster_id=roster_id,
    )
    db.add(db_roster_short)
    db.commit()
    db.refresh(db_roster_short)
    return db_roster_short


def read_roster_short(
    db: Session, *, skip: int = 0, limit: int = 100
) -> List[RosterShort]:
    return db.query(RosterShort).offset(skip).limit(limit).all()


def read_user_roster_short(user_id: UUID, db: Session) -> List[RosterShort]:
    db_user = user.get_user_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(RosterShort).filter(RosterShort.user_id == user_id).all()


def read_accepted_user_roster_short(user_id: UUID, db: Session) -> List[RosterShort]:
    db_user = user.get_user_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(RosterShort).join(Roster).filter(Roster.response == "Accept").all()
