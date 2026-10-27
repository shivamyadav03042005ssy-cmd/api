from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Student , StundentDB



def create_student(db :Session ,student:Student):
    new_student = StundentDB(name = student.name ,age = student.age ,course = student.course)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message":"student created successfully","id":new_student.id,"name":new_student.name}


def get_students(db:Session ,page_no:int= 1):
    limit = 10
    offset =(page_no-1)*limit
    Students = (db.query(StundentDB).order_by(StundentDB.id).offset(offset).limit(limit).all())
    return [{"id":student.id, "name": student.name ,"age":student.age , "course": student.course} for student in Students]


def get_student(db:Session,student_id:int):
    student =  (db.query(StundentDB).filter(StundentDB.id==student_id).first())
    if student is None:
        raise HTTPException(status_code=404 ,detail = "Student not found")
    return {"id":student.id , "name":student.name ,"age":student.age , "course": student.course} 


def update_student(db:Session,student_id:int ,student:Student):
    existing_student = (db.query(StundentDB).filter(StundentDB.id==student_id).first())
    if existing_student is None :
        raise HTTPException(status_code=404,detail= "student not found")
    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.course = student.course
    db.commit()
    db.refresh(existing_student)
    return {"message":"student updated succesfully"}

def delete_student(db :Session,student_id:int):
    student = (db.query(StundentDB).filter(StundentDB.id == student_id).first())
    if student is None:
        raise HTTPException(status_code=404,detail= "student not found")
    db.delete(student)
    db.commit()
    return{"message":"student deleted succesfully"}

def search_student(db : Session ,name:str | None = None,course :str | None = None ):
    query = db.query(StundentDB)
    if name :
        query = query.filter(StundentDB.name.ilike(f"%{name}%"))
    if course:
        query = query.filter(StundentDB.course.ilike(f"%{course}%"))
    students= query.order_by(StundentDB.id).all()
    return [{"id":student.id,"name":student.name,"course":student.course} for student in students]
