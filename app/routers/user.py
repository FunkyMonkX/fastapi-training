from http.client import HTTPException
from fastapi import status, status,HTTPException,Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",response_model=schemas.UserOut)
def create_posts(user:schemas.UserCreate, db: Session = Depends(get_db)):
    
    #hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict()) #tego tutaj nie kumam - tam nizej nie potrzeba gwiazdek, co robia gwiazdki?
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id:int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")

    return user