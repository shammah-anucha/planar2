from fastapi import APIRouter
from datetime import date
from fastapi import Depends
from sqlalchemy.orm import Session
from ....app.modules.unavailability.schema import Unavailability, UnavailabilityCreate
from ....app.modules.unavailability.crud import unavailabilities
from ....app.modules.notification.crud import send_notification
from ....app.modules.notification.schema import NotificationCreate
from ....app.modules.events.model import Event
from ....app.modules.common.db.session import get_db
from ....app.modules.unavailability.routes import unavailability_router
from ....app.modules.users.routes import user_router
from ....app.modules.events.routes import event_router
from ....app.modules.departments.routes import department_router
from ....app.modules.users.login import login_router
from ....app.modules.common.email.routes import email_router


api_router = APIRouter(dependencies=[Depends(get_db)])


api_router.include_router(login_router)
api_router.include_router(user_router)
api_router.include_router(event_router)
api_router.include_router(department_router)
api_router.include_router(email_router)
api_router.include_router(unavailability_router)


# works
@api_router.get("/upcoming_events/")
def read_upcoming_events(db: Session = Depends(get_db)):
    return db.query(Event).filter(Event.date >= date.today()).all()


# set available days in a week/month
@api_router.post("/users/unavailability/{user_id}", response_model=Unavailability)
def set_unavailability(
    user_id: int, days: UnavailabilityCreate, db: Session = Depends(get_db)
):
    # if user_login:
    #     models.Unavailabilities.user_id = days.user_id
    return unavailabilities.set_user_unavailable(db=db, days=days, user_id=user_id)


@api_router.get("/user/notification/{from_user}/{to_user}")
def notification(
    from_user: int,
    to_user: int,
    db: Session = Depends(get_db),
):
    return send_notification(from_user=from_user, db=db, to_user=to_user)
