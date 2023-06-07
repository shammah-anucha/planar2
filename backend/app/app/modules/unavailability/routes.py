from fastapi import APIRouter, Depends
from typing import Any, List
from .crud import unavailabilities
from ....app.modules.common.email.crud import crud_email
from ....app.modules.common.db.session import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from ....app.modules.unavailability.schema import Unavailability, UnavailabilityCreate


unavailability_router = APIRouter(
    prefix="/users",
    tags=["unavailability"],
    dependencies=[Depends(get_db)],
)


# Admin on sends invites to available users only
# @unavailability_router.get("/{user_id}/unavailability/auth={authToken}")
# def get_unavailabilities(
#     skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
# ):
#     return unavailabilities.get_user_unavailable(db, skip=skip, limit=limit)


# @unavailability_router.get("/{user_id}/unavailability/emails")
# def get_available_emails(db: Session = Depends(get_db)):
#     return crud_email.get_available_emails(db=db)


@unavailability_router.get(
    "/unavailabilities/{user_id}", response_model=List[Unavailability]
)
def get_user_vacations(
    user_id: UUID,
    db: Session = Depends(get_db),
):
    return unavailabilities.get_user_vacation(db=db, user_id=user_id)


# set available days in a week/month
@unavailability_router.post("/unavailability/{user_id}", response_model=Unavailability)
def set_unavailability(days: UnavailabilityCreate, db: Session = Depends(get_db)):
    # if user_login:
    #     models.Unavailabilities.user_id = days.user_id
    return unavailabilities.set_user_unavailable(db=db, days=days)
