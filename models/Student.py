from sqlalchemy import Column, Integer, String

from config.db import Base


class Student(Base):
    __tablename__ = "student"

    id_student = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    age = Column(Integer)
