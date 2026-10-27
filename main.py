from fastapi import FastAPI ,Query,Depends
from sqlalchemy.orm import Session
from models import Student , StundentDB
from database import base,engine,get_db
import crud

app = FastAPI(title="student Management API")

base.metadata.create_all(bind=engine)

@app.post("/student")
def create_student(student:Student,db:Session = Depends(get_db)):
   return crud.create_student(db,student)

@app.get("/students")
def get_students(page_no:int = Query(default=1, ge=1) ,db:Session = Depends(get_db)):
   return crud.get_students(db,page_no)


@app.put("/student/{studnet_id}")
def update_student(student_id:int ,student:Student,db:Session = Depends(get_db)):
    return crud.update_student(db,student_id,student)

@app.get("/students/search_student")
def search_student(name:str |None = None , course : str |None = None,db :Session = Depends(get_db)):
    return crud.search_student(db,name,course)

@app.get("/students/{student_id}")
def get_student(student_id:int ,db :Session = Depends(get_db)):
    return crud.get_student(db,student_id)

@app.delete("/students/{student_id}")
def delete_student(student_id:int,db:Session = Depends(get_db)):
    return crud.delete_student(db,student_id)