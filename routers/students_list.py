from fastapi import APIRouter
from .students_data import students

router = APIRouter()


@router.get("/students")
def get_students():
    return students
