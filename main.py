
from fastapi import FastAPI

from routers import (
    students_list,
    student_detail,
    student_create,
    student_update,
    student_delete,
)

app = FastAPI(title="Shihab Ahmed ")

app.include_router(students_list.router)
app.include_router(student_detail.router)
app.include_router(student_create.router)
app.include_router(student_update.router)
app.include_router(student_delete.router)


@app.get("/")
def home():
    return {"message": "Student Management API is running"}
