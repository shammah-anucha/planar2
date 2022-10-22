# Import all the models, so that Base has them before being
# imported by Alembic
from app.modules.common.db.base_class import Base  # noqa
from app.modules.departments import model  # noqa
from app.modules.events import model
from app.modules.messages import model
from app.modules.notification import model
from app.modules.roster import model
from app.modules.unavailability import model
from app.modules.userdepartment import model
from app.modules.users import model
