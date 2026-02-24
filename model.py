from sqlalchemy import Column,Integer,VARCHAR
from database import Base

class STUDENT(Base):
    __tablename__="students"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(VARCHAR(255))
    branch=Column(VARCHAR(255))
    dob=Column(VARCHAR(255))