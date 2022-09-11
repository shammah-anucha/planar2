import os
from fastapi import BackgroundTasks, Depends
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from typing import Optional, List
import crud, models
from crud import get_db

from sqlalchemy.orm import Session

from dotenv import load_dotenv

load_dotenv(".env")


class Envs:
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM = os.getenv("MAIL_FROM")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME = os.getenv("MAIN_FROM_NAME")


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER="./templates/email",
)


async def send_email_async(subject: str, email_to: str, body: str):
    message = MessageSchema(
        subject=subject, recipients=[email_to], body=body, subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html")


def send_email_background(
    background_tasks: BackgroundTasks, subject: str, email_to: List[str], body: str
):
    message = MessageSchema(
        subject=subject, recipients=email_to, body=body, subtype="html"
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name="email.html")


def collect_email_db(db: Session):
    for user in db.query(models.User).all():
        return models.User.email
        # if models.User.unavailabilities is None:

    # all_user_id = db.query(models.User).filter(models.User.user_id).all()
    # for user_id in all_user_id:
    #     if user_id not in models.Unavailabilities.user_id:
    #         return user_id
