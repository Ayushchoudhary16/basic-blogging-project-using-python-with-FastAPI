from fastapi import HTTPException, Request,Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt

from app.dtos import *
from app.model import *





SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(normal_password, hashed_password):
    return pd_context.verify(normal_password, hashed_password)

def get_password_hash(password):
    return pd_context.hash(password)


def get_user_by_username(username:str,db:Session):
    user=db.query(User).filter(User.username==username).first()
    if not user:
        return None
    return user

def registerUser(body:userSchema,db:Session):
    username=get_user_by_username(body.username,db)
    if username:
        raise HTTPException(409,detail={"message":"user name is already exits"})
    
    newUser=User(name=body.name,email=body.email,username=body.username,password=get_password_hash(body.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return{
        "status":"okk",
        "User":newUser
    }
    
def loginUser(body:loginSchema,db:Session):
    user=get_user_by_username(body.username,db)
    if not user:
        raise HTTPException(404,detail={"message":"user name is not exits"})
    
    password=verify_password(body.password,user.password)
    if not password:
        raise HTTPException(404,detail={"message":"password is not correct"})
    
    expire_time=datetime.now(timezone.utc)+timedelta(minutes=5)
    token=jwt.encode({"username":user.username,"exp":expire_time},SECRET_KEY,algorithm=ALGORITHM)

    return {
        "massage":"okk",
        "token":token
    }







