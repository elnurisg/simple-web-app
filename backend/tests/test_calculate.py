import pytest
from backend.calculate import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, -2) == -3
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(-1, -1) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 2) == -2
    assert multiply_numbers(0, 5) == 0

def test_divide_numbers():
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(10, 2) == 5
    with pytest.raises(ValueError):
        divide_numbers(1, 0)
