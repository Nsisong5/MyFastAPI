from sqlalchemy import String, Integer, Boolean, Column 
#from sqlalchemy.ext import null
from database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text,null


class Product(Base):
     __tablename__ = "products"
     id = Column(Integer, primary_key=True, nullable=False)
     name = Column(String, nullable=False )
     brand = Column(String, nullable=False)
     created = Column(TIMESTAMP(timezone=True),server_default=text("Now()"), nullable=False)
     
     
     
     
     