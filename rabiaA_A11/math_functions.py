# math_functions.py

def power(base, exponent):
    """Raise a number to a power."""
    return base ** exponent

def divide(numerator, denominator):
    """Divide two numbers."""
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return numerator / denominator

