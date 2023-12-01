from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing_extensions import Optional

from models.Student import Student


class StudentBase(BaseModel):
    id: Optional[int]
    nom: str
    prenom: str
    age: int

    class Config:
        orm_mode = True

    @staticmethod
    def get(db: Session):
        return db.query(Student).all()
