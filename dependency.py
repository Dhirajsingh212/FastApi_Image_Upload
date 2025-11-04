from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session

from database.db import get_db

db_dependecy = Annotated[Session,Depends(get_db)]
