from typing import List
from datetime import timedelta, date
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from crud import authenticate_user, create_access_token, get_db
from schemas import Token
import crud, models, schemas, send_email
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency


# works
@app.post("/login/access-token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif crud.disabled(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(user.user_id, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}


# works
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# works
@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)


# works
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# works
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.user_id == user_id).delete()
    db.commit()
    return "Delete Successful"


@app.post(
    "/users/{user_id}/{event_id}/{Firstname}/{Lastname}/roster",
    response_model=schemas.RosterCreate,
)
def create_event_for_user(
    user_id: int,
    event_id: int,
    Firstname: str,
    Lastname: str,
    roster: schemas.EventCreate,
    db: Session = Depends(get_db),
):
    return crud.create_roster(
        user_id=user_id,
        event_id=event_id,
        roster=roster,
        db=db,
        Firstname=Firstname,
        Lastname=Lastname,
    )


# works
@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roster = crud.get_events(db, skip=skip, limit=limit)
    return roster


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


# Admin on sends invites to available users only
@app.get("/unavailability/")
def get_unavailabilities(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_user_unavailable(db, skip=skip, limit=limit)


@app.get("/unavailability/emails")
def get_available_emails(db: Session = Depends(get_db)):
    return crud.get_available_emails(db=db)


@app.get("/send-email/asynchronous")
async def send_email_asynchronous():
    await send_email.send_email_async(
        "Hello World", "tracy2anucha@gmail.com", "Hello World"
    )
    return "Success"


@app.get("/send-email/backgroundtasks")
def send_email_backgroundtasks(background_tasks: send_email.BackgroundTasks):
    send_email.send_email_background(
        background_tasks, "Hello World", "tracy2anucha@gmail.com", "Hello World"
    )
    return "Success"


# departments
@app.post("/departments/", response_model=schemas.Department)
def create_department(
    department: schemas.DepartmentCreate, db: Session = Depends(get_db)
):
    return crud.create_department(db=db, department=department)


@app.get("/departments/", response_model=List[schemas.Department])
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_department(db, skip=skip, limit=limit)


# is it neccessary to create a schema for user_department
@app.post("/users/departments/{user_id}/{dept_id}")
def assign_department(user_id: int, dept_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_id(db, id=user_id)
    db_dept = crud.get_dept_id(db, id=dept_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.assign_department(user_id=user_id, dept_id=dept_id, db=db)
    # TODO avoid repeating the same entry


@app.get("/user/departments/")
def get_user_departments(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_user_department(db, skip=skip, limit=limit)


@app.get("/send-email/departments/{dept_id}")
def send_emails_by_dept(
    background_tasks: send_email.BackgroundTasks,
    dept_id: int,
    db: Session = Depends(get_db),
):
    email_dept_available = []
    db_dept = crud.get_dept_id(db, id=dept_id)
    get_email = crud.get_available_emails(db=db)
    get_email_dept = crud.get_email_in_department(db=db, dept_id=dept_id)
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    for email in get_email_dept:
        if email in get_email:
            email_dept_available.append(email)
    send_email.send_email_background(
        background_tasks, "Hello World", email_dept_available, "Hello World"
    )
    return "Success"
    # TODO remove unavailable emails that have passed the time frame
