from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str


class MessageCreate(MessageBase):
    pass


class MessageUpdate(MessageBase):
    pass


class Message(MessageBase):
    msg_id: int
    user_id: int

    class Config:
        orm_mode = True


class MessageForm(BaseModel):
    invitation: str = "You have been invited to serve"
    please_respond: str = "Please respond to request Accept or Decline"
