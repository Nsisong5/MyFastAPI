from fastapi import FastAPI 

from database import get_db, engine 
from routers import product 
import models 

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(product.router)
