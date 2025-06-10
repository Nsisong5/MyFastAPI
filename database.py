from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config import settings 

MY_URL = f"{settings.database}://{settings.database_username}:{settings.database_user_password}@{settings.database_host_name}/{settings.database_name}"

Base = declarative_base()


engine = create_engine(MY_URL)

Sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
     db = Sessionlocal()
     try:
          yield db
     finally:
          db.close()





