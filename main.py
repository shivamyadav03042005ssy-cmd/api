from fastapi import FastAPI ,Query
from models import Student
#from database import get_connection
import crud

app = FastAPI()

@app.post("/student")
def create_student(student:Student):
   return crud.create_student(student)

@app.get("/students")
def students(page_no:int = Query(default=1, ge=1)):
   return crud.students(page_no)


@app.put("/student/{studnet_id}")
def update_student(student_id:int ,student:Student):
    return crud.update_student(student_id,student)

@app.get("/students/search_student")
def search_student(name:str |None = None , course : str |None = None):
    return crud.search_student(name,course)

@app.get("/students/{student_id}")
def get_student(student_id:int):
    return crud.get_student(student_id)

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    return crud.delete_student(student_id)


    
