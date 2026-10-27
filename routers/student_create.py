
from fastapi import APIRouter
from pydantic import BaseModel
from .students_data import students

router = APIRouter()


class StudentCreate(BaseModel):
    name: str
    age: int
    department: str


@router.post("/students", status_code=201)
def create_student(student: StudentCreate):
    new_id = max(
        (item["id"] for item in students),
        default=0
    ) + 1

    new_student = {
        "id": new_id,
        **student.model_dump()
    }

    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }
