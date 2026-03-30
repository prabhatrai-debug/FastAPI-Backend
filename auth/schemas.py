from pydantic import BaseModel, EmailStr

#schema for new user create 
class userCreates(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str

#schema for user login
class UserLogiin(BaseModel):
    username:str
    password:str

