from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
   id: int
   name :str = Field(None, title="The description of the item", max_length=50)
   subjects: List[str] = Field([], title="The description of the item", max_length=3)

data = {
   'id': 1,
   'name': 'Soumit Kundu',
   'subjects': ["Eng", "Math", "Sc"],
}

@app.get("/")
def index():
    return {"message": "Welcome to AI Automator!"}

@app.get("/hello")
def hello(name: str, age: int):
    return {"Hello": name, "age": age}

@app.get("/student")
def get_student():
    s1=Student(**data)
    return s1

@app.post("/students/")
async def student_data(s1: Student):
   return {'message': 'Student data received', 'data': s1}

# When run normally, like: py main.py | then uncomment the below code
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="localhost", port=8090, reload=True)
# Otherwise run through uvicorn command, like: uvicorn main:app --host localhost --port 8090 --reload | no need to uncomment the above code