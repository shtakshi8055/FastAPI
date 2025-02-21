from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow Cross-Origin Resource Sharing (CORS) (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],  # Allow all domains (change for security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define input data schema
class InputData(BaseModel):
    data: List[str]

# ✅ Home Route for Testing
@app.get("/")
def home():
    return {"message": "FastAPI server is running!"}

# ✅ GET API to return operation code
@app.get("/operation")
def get_operation_code():
    return {"operation_code": "ABC123"}

# ✅ POST API to process data
@app.post("/process")
def process_data(input_data: InputData):
    if not input_data.data:
        raise HTTPException(status_code=400, detail="Input data list cannot be empty.")

    numbers = [item for item in input_data.data if item.isdigit()]
    alphabets = [item for item in input_data.data if item.isalpha()]
    highest_alphabet = max(alphabets, key=lambda x: x.lower(), default="")

    response = {
        "status": "success",
        "user_id": "123456",
        "college_email": "user@college.edu",
        "college_roll_number": "CS2024001",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

    return response
