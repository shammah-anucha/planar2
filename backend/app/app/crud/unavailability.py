from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...app.crud.base import CRUDBase
from ...app.models.unavailability import Unavailabilities
from ...app.schemas.unavailability import UnavailabilityCreate


class CRUDUnavailability(CRUDBase[Unavailabilities, UnavailabilityCreate]):
    def set_user_unavailable(self, db: Session, *, obj_in: UnavailabilityCreate):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # TODO remove unavailable emails that have passed the time frame
    def get_user_unavailable(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[Unavailabilities]:
        return db.query(self.model).offset(skip).limit(limit).all()


unavailability = CRUDUnavailability(Unavailabilities)
