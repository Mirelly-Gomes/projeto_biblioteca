from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///./estoque.db", connect_args={"check_same_thread": False})

Session_Local = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()