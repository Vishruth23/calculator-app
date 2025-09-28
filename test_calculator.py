import pytest
from calculator import sqrt, factorial, log, power
import math

def test_sqrt():
    assert sqrt(16) == 4

def test_sqrt_negative():
    with pytest.raises(ValueError, match="Cannot compute square root"):
        sqrt(-5)

def test_factorial():
    assert factorial(5) == 120


def test_log():
    assert(log(math.e) == 1)
    

def test_power():
    assert power(2, 4) == 16
