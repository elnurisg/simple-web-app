import pytest
from backend.utils import next_prime, is_prime

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True

def test_next_prime():
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(5) == 7
    assert next_prime(10) == 11
    assert next_prime(14) == 17
