from fastapi import APIRouter, Depends, HTTPException
from .....app import utils
from .....app.api import deps
from ....crud.departments import department
from ....crud.emails import crud_email
from ....crud.userdept import userdept
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/send_email", tags=["send_email"], dependencies=[Depends(deps.get_db)]
)


@router.get("/asynchronous")
async def send_email_asynchronous():
    await utils.send_email_async("Hello World", "tracy2anucha@gmail.com", "Hello World")
    return "Success"


@router.get("/backgroundtasks")
def send_email_backgroundtasks(background_tasks: utils.BackgroundTasks):
    utils.send_email_background(
        background_tasks, "Hello World", "tracy2anucha@gmail.com", "Hello World"
    )
    return "Success"


@router.get("/departments/{dept_id}")
def send_emails_by_dept(
    background_tasks: utils.BackgroundTasks,
    dept_id: int,
    db: Session = Depends(deps.get_db),
):
    email_dept_available = []
    db_dept = department.get_dept_id(db, id=dept_id)
    get_email = crud_email.get_available_emails(db=db)
    get_email_dept = userdept.get_email_in_department(db=db, dept_id=dept_id)
    if db_dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    for email in get_email_dept:
        if email in get_email:
            email_dept_available.append(email)
    utils.send_email_background(
        background_tasks, "Hello World", email_dept_available, "Hello World"
    )
    return "Success"
    # TODO remove unavailable emails that have passed the time frame
