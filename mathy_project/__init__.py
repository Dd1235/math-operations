from typing import (
    Union,
)  # for typechecking so that only numbers can be added and not strings, lists etc

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Add two numbers together"""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Subtract two numbers together"""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return x - y


def multiply(x: Number, y: Number) -> Number:
    """Multiply two numbers together"""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return x * y
