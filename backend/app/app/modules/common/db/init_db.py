from sqlalchemy.orm import Session

# from ...app import crud, schemas
# from ...app.core.config import settings

# from ...app.db import base  # noqa: F401

# from ...app.db.base_class import Base  # noqa
# from ...app.db.session import engine, Base

# Base.metadata.create_all(engine)
# def init_db() -> None:
# Tables should be created with Alembic migrations
# But if you don't want to use migrations, create
# the tables un-commenting the next line
# Base.metadata.create_all(bind=engine)

# user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
# if not user:
#     user_in = schemas.UserCreate(
#         email=settings.FIRST_SUPERUSER,
#         password=settings.FIRST_SUPERUSER_PASSWORD,
#         is_admin=True,
#     )
#     user = crud.user.create_user(db, obj_in=user_in)  # noqa: F841
