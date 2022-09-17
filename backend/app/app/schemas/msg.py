from pydantic import BaseModel


class MessageBase(BaseModel):

    message: str = "You have been invited to serve"


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    msg_id: int
    user_id: int

    class Config:
        orm_mode = True
