from datetime import date
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from api import crud, models, schemas
from .database import engine
from .dependencies import get_db
from .routers import events, users, departments, email, unavailability, login


models.Base.metadata.create_all(bind=engine)


app = FastAPI(dependencies=[Depends(get_db)])


app.include_router(login.router)
app.include_router(users.router)
app.include_router(events.router)
app.include_router(departments.router)
app.include_router(email.router)
app.include_router(unavailability.router)


# works
@app.get("/upcoming_events/")
def read_upcoming_events(db: Session = Depends(get_db)):
    return db.query(models.Event).filter(models.Event.date >= date.today()).all()


# set available days in a week/month
@app.post("/users/unavailability/{user_id}", response_model=schemas.Unavailability)
def set_unavailability(
    user_id: int, days: schemas.UnavailabilityCreate, db: Session = Depends(get_db)
):
    # if user_login:
    #     models.Unavailabilities.user_id = days.user_id
    return crud.set_user_unavailable(db=db, days=days, user_id=user_id)


@app.get("/user/notification/{from_user}/{to_user}")
def notification(from_user: int, to_user: int, db: Session = Depends(get_db)):
    return crud.send_notification(from_user=from_user, db=db, to_user=to_user)
