from datetime import timedelta
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..dependencies import get_db
from api import crud, schemas
from ..crud import authenticate_user, create_access_token
from ..schemas import Token


router = APIRouter(prefix="/login", tags=["login"], dependencies=[Depends(get_db)])

# works
@router.post("/access-token", response_model=Token)
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
