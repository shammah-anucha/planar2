import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ..app.modules.common.api import api_router
from ..app.modules.common.utils.core.config import settings
from ..app.modules.common.db.session import engine
from ..app.modules.common.db.base_class import Base


# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_creditials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


# if __name__ == "__main__":
#     uvicorn.run(app, port=8000, host="0.0.0.0")
