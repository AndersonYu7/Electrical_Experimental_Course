import math

def square_root(a):
    """Return the square root of a given number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)
