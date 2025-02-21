from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],  # Change "*" to your frontend URL after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    data: List[str]

@app.get("/")
def home():
    return {"message": "FastAPI server is running!"}

@app.get("/operation")
def get_operation_code():
    return {"operation_code": "ABC123"}

@app.post("/process")
def process_data(input_data: InputData):
    if not input_data.data:
        return {"status": "error", "message": "Input data cannot be empty"}

    numbers = [item for item in input_data.data if item.isdigit()]
    alphabets = [item for item in input_data.data if item.isalpha()]
    highest_alphabet = max(alphabets, key=lambda x: x.lower(), default="")

    return {
        "status": "success",
        "user_id": "123456",
        "college_email": "user@college.edu",
        "college_roll_number": "CS2024001",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
