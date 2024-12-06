#!/usr/bin/env python3

import math

"""
This module contains a function `floor` that takes a float value
as an argument and returns the floor of that float.
It demonstrates the use of the math module and type annotations.
"""


def floor(n: float) -> int:
    """
    Returns the floor of the given float number.

    The floor of a number is the largest integer less than or equal
    to the number. For example, the floor of 3.14 is 3.

    Parameters:
    n (float): The number to compute the floor value of.

    Returns:
    int: The floor value of the input float.
    """
    return math.floor(n)
