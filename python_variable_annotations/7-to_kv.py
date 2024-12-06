#!/usr/bin/env python3

"""
This module contains a function `to_kv` that creates a tuple with a string
and the square of a given number. It demonstrates the use of type annotations
and the ability to work with both integers and floating-point numbers.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a number.

    This function takes a string and a number (either integer or float),
    squares the number, and returns a tuple where the first element is
    the string and the second element is the square of the number as a float.

    Parameters:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The number (or a float) to be squared.

    Returns:
    Tuple[str, float]: and the square of the number as a float.
    """
    return (k, float(v ** 2))
