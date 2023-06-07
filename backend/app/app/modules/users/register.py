from datetime import timedelta
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import crud, utils, schema
from ....app.modules.common.utils.core.config import settings
from ....app.modules.common.utils.core import security
from ....app.modules.common.utils.token import Token
from fastapi import FastAPI, Request


register_router = APIRouter(
    prefix="/register", tags=["authenticate"], dependencies=[Depends(utils.get_db)]
)


# works
@register_router.post("/", response_model=Token)
async def login_for_access_token(
    *,
    users_in: schema.UserCreate,
    request: Request,
    db: Session = Depends(utils.get_db),
):
    # data = await request.json()
    user = crud.user.get_user_by_email(db, email=users_in.email)
    # user = crud.user.authenticate_user(
    #     db, email=data.get("username"), password=data.get("password")
    # )
    # if not user:
    #     raise HTTPException(status_code=400, detail="Incorrect email or password")
    # elif crud.user.disabled(user):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = security.create_access_token(
            user.user_id, expires_delta=access_token_expires
        )

        crud.user.create(db=db, obj_in=users_in)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.user_id,
    }


# @user_router.post("/users/{user_id}", response_model=User, tags=["users"])
# def create_user(*, users_in: UserCreate, db: Session = Depends(utils.get_db)) -> Any:
#     """Create new user."""
#     user = crud.user.get_user_by_email(db, email=users_in.email)
#     if user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.user.create(db=db, obj_in=users_in)


# @router.post("/login/test-token", response_model=schemas.User)
# def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
#     """
#     Test access token
#     """
#     return current_user


# @router.post("/password-recovery/{email}", response_model=schemas.Msg)
# def recover_password(email: str, db: Session = Depends(deps.get_db)) -> Any:
#     """
#     Password Recovery
#     """
#     user = crud.user.get_by_email(db, email=email)

#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this username does not exist in the system.",
#         )
#     password_reset_token = generate_password_reset_token(email=email)
#     send_reset_password_email(
#         email_to=user.email, email=email, token=password_reset_token
#     )
#     return {"msg": "Password recovery email sent"}


# @router.post("/reset-password/", response_model=schemas.Msg)
# def reset_password(
#     token: str = Body(...),
#     new_password: str = Body(...),
#     db: Session = Depends(deps.get_db),
# ) -> Any:
#     """
#     Reset password
#     """
#     email = verify_password_reset_token(token)
#     if not email:
#         raise HTTPException(status_code=400, detail="Invalid token")
#     user = crud.user.get_by_email(db, email=email)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this username does not exist in the system.",
#         )
#     elif not crud.user.is_active(user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     hashed_password = get_password_hash(new_password)
#     user.hashed_password = hashed_password
#     db.add(user)
#     db.commit()
#     return {"msg": "Password updated successfully"}
