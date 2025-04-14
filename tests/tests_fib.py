"""
Unit tests for the Fibonacci module.
"""

from fibonacci import generate_fibonacci

def test_fibonacci_basic():
    """
    Test basic functionality of the generate_fibonacci function.
    """
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(2) == [0, 1]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_large():
    """
    Test the generate_fibonacci function with a larger input.
    """
    result = generate_fibonacci(10)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result == expected

def test_fibonacci_negative():
    """
    Test the generate_fibonacci function with a negative input.
    """
    assert generate_fibonacci(-3) == "Please enter a positive integer."

def test_fibonacci_zero():
    """
    Test the generate_fibonacci function with zero as input.
    """
    assert generate_fibonacci(0) == "Please enter a positive integer."
