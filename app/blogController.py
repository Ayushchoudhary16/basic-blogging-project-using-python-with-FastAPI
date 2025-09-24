from fastapi import HTTPException, Request,Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt

from app.dtos import *
from app.model import *


def createBlog(body:blogSchema,db:Session,user:User):
    userId=user.id
    newblog=Blog(title=body.title,content=body.content,headerImage=body.headerImage,userId=userId)
    db.add(newblog)
    db.commit()
    db.refresh(newblog)
    return{
        "status":"okk",
        "bolg":newblog
    }

def getBlogs(db:Session):
    blogs=db.query(Blog).all()
    return {
        "status":"okk",
        "bolg": blogs
    }

def deleteBlog(id:int,db:Session,user:User):
    blog=db.query(Blog).filter(Blog.id==id).first()
    
    if not blog.userId==user.id:
        raise HTTPException(404,detail={"message":"your not able to delte this blog"})
    
    db.delete(blog)
    db.commit()
    return{
        "message":'okk',
        "blog":blog
    }


# https://github.com/Ayushchoudhary16/basic-blogging-project-using-python-with-FastAPI