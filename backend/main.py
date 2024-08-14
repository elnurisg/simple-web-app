from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculate import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

app = FastAPI()

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

    if operation == "add":
        result = add_numbers(a, b)
    elif operation == "subtract":
        result = subtract_numbers(a, b)
    elif operation == "multiply":
        result = multiply_numbers(a, b)
    elif operation == "divide":
        try:
            result = divide_numbers(a, b)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")

    return {"result": result}
