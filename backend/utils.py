from math import sqrt

# Checks if n is prime: handles small numbers, skips even and multiples of 3, 
# tests up to sqrt(n) using 6k ± 1 optimization.
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n: int) -> int:
    """Find the first prime number greater than n."""

    # if it is less or equal than 2, the next prime number will be 2 
    # bcz prime numbers can not be negative and >=2
    if n <= 2: 
        return 2
    
    prime = n + 1
    while not is_prime(prime):
        prime += 1
    return prime
