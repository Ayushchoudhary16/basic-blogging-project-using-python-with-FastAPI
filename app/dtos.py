from pydantic import BaseModel

class userSchema(BaseModel):
    name:str
    email:str
    username:str
    password:str

class loginSchema(BaseModel):
    username:str
    password:str

class blogSchema(BaseModel):
    title:str
    content:str
    headerImage:str

class studentSchema(BaseModel):
    title:str
    content:str
    headerImage:str