from app.utills.db import *
from sqlalchemy.orm import Session
from sqlalchemy import Column,Integer,String,ForeignKey
from fastapi import Request,HTTPException

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String,unique=True)
    username = Column(String, unique=True, nullable=False)
    password=Column(String)


class Blog(Base):
    __tablename__="blog"

    id=Column(Integer,primary_key=True)
    
    title=Column(String)
    content=Column(String)
    headerImage=Column(String)
    userId=Column(Integer,ForeignKey("users.id"))