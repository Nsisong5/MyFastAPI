from sqlalchemy.orm import Session
from fastapi import Depends 
from fastapi import APIRouter 
from database import get_db
from fastapi import HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import models 
import schemas 



router = APIRouter()


@router.post("/create")
def get_products(product: schemas.ProductCreate,db: Session=Depends(get_db)):
     product = models.Product(**product.dict())
     db.add(product)
     db.commit()
     db.refresh(product)
     return product 
     
@router.get(f"/detail/{id}")
def get_product(id: int ,db: Session=Depends(get_db)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
          raise HTTPException(status_code="404", detail="object not found")
     return product 
     
    
@router.put("/update/{id}")
def product_update( new_product:schemas.ProductCreate,db: Session=Depends(get_db)):
     product = db.query(models.Product).filter(models.Product.id == id)
     # print(new_product.dict()
     update_data = product.first()
     if not update_data:
          raise HTTPException(status_code="404", detail="object not found")
     product.update(new_product.dict(), synchronize_session=False) 
     db.commit()
     return "success"
     
               
@router.delete("/delete/{id}")
def get_products(id: int ,db: Session=Depends(get_db)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
          raise HTTPException(status_code=404, detail="object not found")
     db.delete(product)
     db.commit()
     return {"detail":"success"}   
     
     
     
@router.get("/")
def get_products(db: Session=Depends(get_db)):
   products = db.query(models.Product).all()
   return products                           