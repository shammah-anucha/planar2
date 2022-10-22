from fastapi import APIRouter, Depends
from .crud import unavailabilities
from ....app.modules.common.email.crud import crud_email
from ....app.modules.common.db.session import get_db
from sqlalchemy.orm import Session


unavailability_router = APIRouter(
    prefix="/unavailability",
    tags=["unavailability"],
    dependencies=[Depends(get_db)],
)

# Admin on sends invites to available users only
@unavailability_router.get("/")
def get_unavailabilities(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return unavailabilities.get_user_unavailable(db, skip=skip, limit=limit)


@unavailability_router.get("/emails")
def get_available_emails(db: Session = Depends(get_db)):
    return crud_email.get_available_emails(db=db)
