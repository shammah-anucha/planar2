from fastapi import APIRouter, Depends
from api import crud
from ..dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/unavailability", tags=["unavailability"], dependencies=[Depends(get_db)]
)

# Admin on sends invites to available users only
@router.get("/")
def get_unavailabilities(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_user_unavailable(db, skip=skip, limit=limit)


@router.get("/emails")
def get_available_emails(db: Session = Depends(get_db)):
    return crud.get_available_emails(db=db)
