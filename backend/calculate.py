# Description: This file contains the functions to perform basic arithmetic operations.

def add_numbers(a: float, b: float) -> float:
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    return a * b

def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
