from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import UUID

from ...modules.common.utils.base import CRUDBase
from ...modules.unavailability.model import Unavailabilities
from ...modules.unavailability.schema import UnavailabilityCreate, UnavailabilityUpdate
from ...modules.users.crud import user


class CRUDUnavailability(
    CRUDBase[Unavailabilities, UnavailabilityCreate, UnavailabilityUpdate]
):
    def set_user_unavailable(
        self,
        db: Session,
        *,
        days: UnavailabilityCreate,
    ):
        db_unavalable_days = self.model(
            startdate=days.startdate,
            enddate=days.enddate,
            reason=days.reason,
            user_id=days.user_id,
        )
        db.add(db_unavalable_days)
        db.commit()
        db.refresh(db_unavalable_days)
        return db_unavalable_days

    # TODO remove unavailable emails that have passed the time frame
    def get_user_unavailable(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[Unavailabilities]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_user_vacation(self, db: Session, user_id: UUID) -> List[Unavailabilities]:
        db_user = user.get_user_id(db, id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return (
            db.query(Unavailabilities).filter(Unavailabilities.user_id == user_id).all()
        )

    # def get_volunteer_response(
    #     self, db: Session, roster_id: int, response: str
    # ) -> Optional[Roster]:
    #     return (
    #         db.query(Roster)
    #         .filter(Roster.roster_id == roster_id)
    #         .filter(Roster.response == response)
    #         .first()
    #     )


unavailabilities = CRUDUnavailability(Unavailabilities)
