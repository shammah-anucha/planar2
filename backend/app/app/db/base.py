# Import all the models, so that Base has them before being
# imported by Alembic
from ...app.db.base_class import Base  # noqa
from ...app.models.events import Event  # noqa
from ...app.models.users import User  # noqa
