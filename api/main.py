from typing import List
from datetime import timedelta, date
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api import crud, models, schemas, send_email
from .crud import authenticate_user, create_access_token
from .schemas import Token
from .database import SessionLocal, engine
from .dependencies import get_db
from .routers import events, users, departments, email, unavailability


models.Base.metadata.create_all(bind=engine)


app = FastAPI(dependencies=[Depends(get_db)])

# Dependency


# works
# @app.post("/login/access-token", response_model=Token)
# async def login_for_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
# ):
#     user = authenticate_user(db, email=form_data.username, password=form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
#     elif crud.disabled(user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(user.user_id, expires_delta=access_token_expires)

#     return {"access_token": access_token, "token_type": "bearer"}


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
