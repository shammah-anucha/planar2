from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ...modules.common.utils.base import CRUDBase
from ...modules.events.model import Event

from ...modules.departments.model import Departments
from ...modules.departments.schema import DepartmentCreate, DepartmentUpdate


class CRUDDepartment(CRUDBase[Departments, DepartmentCreate, DepartmentUpdate]):
    def create_department(
        self, db: Session, *, obj_in: DepartmentCreate
    ) -> Departments:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_department(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Departments]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_dept_id(self, db: Session, id: Any) -> List[Departments]:
        return db.query(Departments.dept_id).filter(Departments.dept_id == id).first()


department = CRUDDepartment(Departments)
