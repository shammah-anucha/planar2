from pydantic import BaseModel


class MessageBase(BaseModel):

    message: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    msg_id: int
    user_id: int

    class Config:
        orm_mode = True
