import math

def sqrt(x):
    if(x<0):
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)

def power(base, exp):
    return math.pow(base, exp)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number")
    return math.factorial(n)

def log(x, base=math.e):
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(x, base)