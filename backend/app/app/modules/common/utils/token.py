from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: UUID


class TokenPayload(BaseModel):
    sub: Optional[int] = None
