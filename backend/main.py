from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculate import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from utils import next_prime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request body 
class CalculatePayload(BaseModel):
    a: int
    b: int
    operation: str

# post endpoint
@app.post("/calculate")
async def calculate(payload: CalculatePayload):
    a = payload.a
    b = payload.b
    operation = payload.operation

    higher_num = max(a, b)
    prime = next_prime(higher_num)

    if operation == "add":
        result = add_numbers(a, b)
        result = add_numbers(result, prime)
    elif operation == "subtract":
        result = subtract_numbers(a, b)
        result = subtract_numbers(result, prime)
    elif operation == "multiply":
        result = multiply_numbers(a, b)
        result = multiply_numbers(result, prime)
    elif operation == "divide":
        try:
            result = divide_numbers(a, b)
            result = divide_numbers(result, prime)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")

    return {"result": result}
