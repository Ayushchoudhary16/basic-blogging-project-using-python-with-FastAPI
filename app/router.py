from fastapi import Depends,Request,APIRouter
from sqlalchemy.orm import Session
from app.controller import *
from app.model import *
from app.dtos import *
from app.blogController import *
from app.utills.is_authentication import*

router=APIRouter()

@router.post("/registerUser")
def create_User(body:userSchema,db:Session=Depends(get_db)):
    return registerUser(body,db)

@router.post("/loginUser")
def login_User(body:loginSchema,db:Session=Depends(get_db)):
    return loginUser(body,db)



@router.post("/createBlog")
def create_User(body:blogSchema,db:Session=Depends(get_db),user:User=Depends(is_authenticated)):
    return createBlog(body,db,user)

@router.get("/getBlog")
def get_blog(db:Session=Depends(get_db)):
    return getBlogs(db)

@router.delete("/deleteBlog")
def delete_blog(id:int,db:Session=Depends(get_db),user:User=Depends(is_authenticated)):
    return deleteBlog(id,db,user)