from fastapi import FastAPI
from models import Student
#from database import get_connection
import crud

app = FastAPI()

@app.post("/student")
def create_student(student:Student):
   return crud.create_student(student)

@app.get("/students")
def students():
   return crud.students()

@app.get("/students/{student_id}")
def get_student(student_id:int):
    return crud.get_student(student_id)

@app.put("/student/{studnet_id}")
def update_student(student_id:int ,student:Student):
    return crud.update_student(student_id,student)

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    return crud.delete_student(student_id)