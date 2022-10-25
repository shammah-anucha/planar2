from typing import List

from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.roster.model import Roster
from ...modules.roster.schema import RosterCreate, RosterUpdate


class CRUDRoster(CRUDBase[Roster, RosterCreate, RosterUpdate]):
    def assign_event(
        self,
        db: Session,
        *,
        event_id: RosterCreate,
        user_id: RosterCreate,
    ) -> Roster:
        db_obj = self.model(user_id=user_id, event_id=event_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


roster = CRUDRoster(Roster)
