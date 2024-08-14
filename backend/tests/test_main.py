from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_calculate_addition():
    response = client.post("/calculate", json={"a": 2, "b": 3, "operation": "add"})
    assert response.status_code == 200
    assert response.json() == {"result": 10} # 3+2=5, 5+5=10

def test_calculate_subtraction():
    response = client.post("/calculate", json={"a": 5, "b": 3, "operation": "subtract"})
    assert response.status_code == 200
    assert response.json() == {"result": -5}  # 5-3=2, 2-7=-5

def test_calculate_multiplication():
    response = client.post("/calculate", json={"a": 2, "b": 3, "operation": "multiply"})
    assert response.status_code == 200
    assert response.json() == {"result": 30}  # 2*3=6, 6*5=30

def test_calculate_division_integer_result(): # 6/2 is integer  
    response = client.post("/calculate", json={"a": 6, "b": 3, "operation": "divide"})
    assert response.status_code == 200
    assert response.json() == {"result": 0}  # 6/3=2, 2/7=0

def test_calculate_division_non_integer_result(): # 7/3 is non-integer
    response = client.post("/calculate", json={"a": 7, "b": 3, "operation": "divide"})
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_calculate_invalid_operation():
    response = client.post("/calculate", json={"a": 2, "b": 3, "operation": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'."}
