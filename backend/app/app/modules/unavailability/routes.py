from fastapi import APIRouter, Depends
from .crud import unavailabilities
from ....app.modules.common.email.crud import crud_email
from ....app.modules.common.db.session import get_db
from sqlalchemy.orm import Session
from ....app.modules.unavailability.schema import Unavailability, UnavailabilityCreate


unavailability_router = APIRouter(
    prefix="/users",
    tags=["unavailability"],
    dependencies=[Depends(get_db)],
)

# Admin on sends invites to available users only
@unavailability_router.get("/{user_id}/unavailability")
def get_unavailabilities(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return unavailabilities.get_user_unavailable(db, skip=skip, limit=limit)


@unavailability_router.get("/{user_id}/unavailability/emails")
def get_available_emails(db: Session = Depends(get_db)):
    return crud_email.get_available_emails(db=db)


# set available days in a week/month
@unavailability_router.post("/{user_id}/unavailability", response_model=Unavailability)
def set_unavailability(
    user_id: int, days: UnavailabilityCreate, db: Session = Depends(get_db)
):
    # if user_login:
    #     models.Unavailabilities.user_id = days.user_id
    return unavailabilities.set_user_unavailable(db=db, days=days, user_id=user_id)
