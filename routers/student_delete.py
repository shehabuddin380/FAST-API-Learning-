
from fastapi import APIRouter, HTTPException
from .students_data import students

router = APIRouter()


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
