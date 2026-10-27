from pydantic import BaseModel,Field
from sqlalchemy import Column, Integer,String
from database import base
class Student(BaseModel):
    name: str = Field(min_length =2 ,max_length= 50)
    age: int = Field(ge = 1 , le =100 )
    course: str = Field(min_length =2 , max_length = 50)
class StundentDB(base):
    __tablename__ ="students"
    id = Column(Integer ,primary_key =True,index = True)
    name =  Column(String,nullable = False)
    age = Column(Integer , nullable = False)
    course  = Column(String , nullable  =False)