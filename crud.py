from fastapi import HTTPException
from database import get_connection
from models import Student



def create_student(student:Student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", (student.name ,student.age,student.course))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return {"message":"student created successfully","id":student_id,"name":student.name}


def students(limit : int = 10 , offset:int = 0):
   
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM students ORDER BY id LIMIT ? OFFSET ?",(limit,offset))
   rows = cursor.fetchall()
   students = [dict(row) for row in rows]
   conn.close()
   return students


def get_student(student_id:int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?",(student_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code =404,detail = "student not found")
    return dict(row)


def update_student(student_id:int ,student:Student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE students SET name = ?, age = ? , course = ?  WHERE id = ?''',(student.name,student.age,student.course,student_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code= 404,detail= "student not found")
    conn.commit()
    conn.close()
    return{"message":"student updated succesfully","id":student_id}



def delete_student(student_id:int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code= 404 , detail="student not found")
    conn.commit()
    conn.close()
    return{"message":"student delete succesfully", "id": student_id}

def search_student(name:str | None = None,course :str | None = None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM students WHERE 1=1"
    params = []
    if name:
        query += " AND LIKE ?"
        params.append(f"%{name}%")
    if cursor:
        query = " AND LIKE ?"
        params.append(f"%{course}%")
    cursor.execute(query,params)
    rows =cursor.fetchall()
    students = [dict(row) for row in rows ]
    conn.close()
    return students


