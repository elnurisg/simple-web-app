# Description: This file contains the functions to perform basic arithmetic operations.

def add_numbers(a: int, b: int) -> int:
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    return int(a - b)

def multiply_numbers(a: int, b: int) -> int:
    return int(a * b)

def divide_numbers(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return int(a / b)
