from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from uuid import UUID

from ...modules.common.utils.base import CRUDBase
from ...modules.unavailability.model import Unavailabilities
from ...modules.unavailability.schema import UnavailabilityCreate, UnavailabilityUpdate


class CRUDUnavailability(
    CRUDBase[Unavailabilities, UnavailabilityCreate, UnavailabilityUpdate]
):
    def set_user_unavailable(
        self, db: Session, *, days: UnavailabilityCreate, user_id: UUID
    ):
        db_unavalable_days = self.model(
            start_date=days.start_date, end_date=days.end_date, user_id=user_id
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


unavailabilities = CRUDUnavailability(Unavailabilities)
