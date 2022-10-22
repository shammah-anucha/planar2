from pydantic import BaseModel


class MessageBase(BaseModel):
    msg_id: int


class MessageCreate(MessageBase):
    pass


class MessageUpdate(MessageBase):
    pass


class Message(MessageBase):
    message: str = "You have been invited to serve"
    user_id: int

    class Config:
        orm_mode = True
