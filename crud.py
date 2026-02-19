from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

students = [
    {
        "id":1,
        "Name":"Raj",
        "Branch":"CSE",
        "dob":"02-05-2005"
    },
    {
        "id":2,
        "Name":"Naman",
        "Branch":"MAE",
        "dob":"01-08-2002"
    },
    {
        "id":3,
        "Name":"ashu",
        "Branch":"MNC",
        "dob":"07-07-2007",
    },
    {
        "id":4,
        "name":"Adi ",
        "Branch":"ECE",
        "dob":"07-04-2005"
    },
   
]

app=FastAPI()

#using get we are fetching data from server 
#here we are fetching students data

@app.get('/student')
def get_student():
    return students

@app.get("/student/{student_id}")
def get_student(student_id:int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="student not found")

class student(BaseModel):
    id:int
    name:str
    Branch:str
    dob:str

@app.post("/student")
def create_student(Student:student):
    new_student=Student.model_dump()
    students.append(new_student)
    return new_student


#to update our data

class studentupdate(BaseModel):
    name:str
    Branch:str
    dob:str
@app.put("/student/{student_id}")
def update_student(student_id:int,student_update:studentupdate):
    for student in students:
        if student["id"]==student_id:
            student['name']=student_update.name
            student['Branch']=student_update.Branch
            student['dob']=student_update.dob
            return student

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")        



#Delete method

@app.delete("/studet/{student_id}")
def delete_student(student_id:int):
    for student in students:
        if student["id"]==student_id:
            students.remove(student)
            return{"message":"our book deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")      