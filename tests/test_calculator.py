import pytest
from calculator.calculator import Calculator

"""Fixture to create a Calculator instance before each test."""
@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-2, 3) == 1
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 3) == -3
    assert calculator.subtract(3, 3) == 0

def test_multiply(calculator):
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(0, 100) == 0
    assert calculator.multiply(-2, 5) == -10

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 3) == 3
    
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        calculator.divide(10, 0)