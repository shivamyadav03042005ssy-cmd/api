from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker
DATABASE_URL = "sqlite:///./student.db"
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
sessionLocal = sessionmaker(autocommit= False,autoflush=False,bind= engine)

base =declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

