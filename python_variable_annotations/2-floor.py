#!/usr/bin/env python3

import math

"""
This module contains a function `floor` that computes the floor of a given float.
It uses the `math` module to calculate the largest integer less than or equal to the provided float.
This module also demonstrates the use of type annotations in Python.
"""


def floor(n: float) -> int:
    """
    Returns the floor of the given float number.

    The floor of a number is the largest integer less than or equal to the number.
    For example, the floor of 3.14 is 3.

    Parameters:
    n (float): The number for which the floor value is computed.

    Returns:
    int: The floor value of the input float.
    """
    return math.floor(n)
