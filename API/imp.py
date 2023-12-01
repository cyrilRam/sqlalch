from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.StudentBase import StudentBase

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/getstudent")
async def getStudents(db: db_dependency):
    return StudentBase.get(db)
