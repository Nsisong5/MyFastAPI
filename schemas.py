from pydantic import BaseModel



class ProductCreate(BaseModel):
     id : int
     name: str
     brand: str