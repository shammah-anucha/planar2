from datetime import time, date

from pydantic import BaseModel


class Responses(BaseModel):
    Accept: str
    Decline: str


class ResponsesUpdate(Responses):
    pass
