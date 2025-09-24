import jwt
from fastapi import Request,HTTPException,Depends
from app.utills.db import get_db
from sqlalchemy.orm import Session
from app.controller import SECRET_KEY,ALGORITHM,get_user_by_username

def is_authenticated(request:Request,db:Session=Depends(get_db)):

    token=request.headers.get("authorization")
    if not token:
        raise HTTPException(404,detail={"message":"token is not found"})
    token=token.split(" ")[-1]
    data=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    user=get_user_by_username(data.get("username"),db)
    if not user:
        raise HTTPException(404,detail={"message":"user not found"})
    return user