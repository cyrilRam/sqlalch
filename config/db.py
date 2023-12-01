from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Remplace ces informations par les tiennes
DB_USER = "s1lyufvzmw1yxji2"
DB_PASSWORD = "lciql5u7rxgqiznu"
DB_HOST = "n2o93bb1bwmn0zle.chr7pe7iynqr.eu-west-1.rds.amazonaws.com"
DB_PORT = "3306"
DB_NAME = "wymz5vpm4rhybfef"

URL_DB = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(URL_DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
