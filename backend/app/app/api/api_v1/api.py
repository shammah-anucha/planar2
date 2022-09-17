from fastapi import APIRouter
from datetime import date
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from api import crud, models, schemas
from db.session import engine
from app.api import deps
from app.api.api_v1 import (
    events,
    users,
    departments,
    email,
    unavailability,
    login,
)

api_router = APIRouter(dependencies=[Depends(deps.get_db)])


api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(events.router)
api_router.include_router(departments.router)
api_router.include_router(email.router)
api_router.include_router(unavailability.router)


# works
@api_router.get("/upcoming_events/")
def read_upcoming_events(db: Session = Depends(deps.get_db)):
    return db.query(models.Event).filter(models.Event.date >= date.today()).all()


# set available days in a week/month
@api_router.post(
    "/users/unavailability/{user_id}", response_model=schemas.Unavailability
)
def set_unavailability(
    user_id: int, days: schemas.UnavailabilityCreate, db: Session = Depends(deps.get_db)
):
    # if user_login:
    #     models.Unavailabilities.user_id = days.user_id
    return crud.set_user_unavailable(db=db, days=days, user_id=user_id)


@api_router.get("/user/notification/{from_user}/{to_user}")
def notification(from_user: int, to_user: int, db: Session = Depends(deps.get_db)):
    return crud.send_notification(from_user=from_user, db=db, to_user=to_user)
