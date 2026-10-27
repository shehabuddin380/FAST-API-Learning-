
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .students_data import students

router = APIRouter()


class StudentUpdate(BaseModel):
    name: str
    age: int
    department: str


@router.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_data: StudentUpdate
):
    for student in students:
        if student["id"] == student_id:
            student.update(updated_data.model_dump())

            return {
                "message": "Student updated successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
