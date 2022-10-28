# import re
# from typing import List, Optional
# from fastapi import Depends
# from ....app.modules.common.db.session import get_db

# from sqlalchemy.orm import Session

# from ...modules.common.utils.base import CRUDBase
# from ...modules.users.model import Users
# from . import model
# from ...modules.roster.model import Roster
# from ...modules.responses.schema import Responses, ResponsesUpdate


# class CRUDResponses(CRUDBase[model.Responses, Responses, ResponsesUpdate]):
#     def response_model(
#         self, db: Session, *, user_id: int, response: Responses
#     ) -> model.Responses:
#         response = str(db.query(model.Responses.response).filter(model.Responses.user_id == user_id).all())
#         if response == 'Accept':


#         # Firstname = (re.search(r"(\w+)", Firstname)).group(0)

#         # db_obj = self.model(user_id=user_id,Firstname=Firstname,Lastname=Lastname,)
#         # db.add(db_obj)
#         # db.commit()
#         # db.refresh(db_obj)
#         # return db_obj

#     def read_roster(
#         self, db: Session, *, skip: int = 0, limit: int = 100
#     ) -> List[Users]:
#         return db.query(self.model).offset(skip).limit(limit).all()


# roster = CRUDResponses(model.Responses)
