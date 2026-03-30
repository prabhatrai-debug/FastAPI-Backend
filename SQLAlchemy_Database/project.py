from fastapi import FastAPI,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
import model 
from pydantic import BaseModel

app=FastAPI()

class StudentData(BaseModel):
    id:int
    name:str
    branch:str
    dob:str

@app.post("/students")
def create_student(student:StudentData,db:Session=Depends(get_db)):
    new_student=model.STUDENT(id=student.id,name=student.name,branch=student.branch, dob=student.dob)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
                   
                   
