from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional,Dict
from pydantic import BaseModel

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class StudentDB(Base):
    __tablename__ = "Student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class Persons(BaseModel):
    id: int
    name: str

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.post("/api")
def create_person(person: Persons):
    db_student = StudentDB(id=person.id, name=person.name)
    db = SessionLocal()
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return {"message": "Student created successfully", "student_data": person.dict()}

@app.get("/api/{id}")
def get_person(id: int):
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.id == id).first()
    db.close()
    if student is None:
        return {"message": "Student not found"}
    return {"student_data": {"id": student.id, "name": student.name}}

@app.put("/api/{id}")
async def update_person(id: int,  update_person: Persons):
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.id == id).first()
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Update the student data based on the updated_person input
    student.id = update_person.id
    student.name = update_person.name
    
    db.commit()
    db.close()
    return {"message": "Student updated successfully", "student_data": update_person.dict()}

@app.delete("/api/{user_Id}")
async def delete_person(id: int):
    db = SessionLocal()
    student = db.query(StudentDB).filter(StudentDB.id == id).first()
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()
    db.close()
    return {"message": "Student deleted successfully"}
