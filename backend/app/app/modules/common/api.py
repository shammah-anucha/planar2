from fastapi import APIRouter
from fastapi import Depends
from ....app.modules.notification.schema import NotificationCreate
from ....app.modules.common.db.session import get_db
from ....app.modules.unavailability.routes import unavailability_router
from ....app.modules.users.routes import user_router
from ....app.modules.events.routes import event_router
from ....app.modules.departments.routes import department_router
from ....app.modules.users.login import login_router

from ....app.modules.roster.routes import roster_router
from ....app.modules.common.email.routes import email_router

# from ....app.modules.association.routes import volunteer_router

api_router = APIRouter(dependencies=[Depends(get_db)])


api_router.include_router(login_router)
api_router.include_router(user_router)
api_router.include_router(event_router)
api_router.include_router(department_router)
api_router.include_router(email_router)
api_router.include_router(unavailability_router)
api_router.include_router(roster_router)
