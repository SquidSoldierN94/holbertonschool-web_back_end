#!/usr/bin/env python3

"""
This module provides a function the floor of a given float number.
It uses the the largest integer less than or equal to the provided float.
The module demonstrates type annotations for better code clarity.
"""


import math


def floor(n: float) -> int:

    """
    Returns the floor of the given float number.

    The floor of than or equal to the number.
    For example, the floor of 3.14 is 3.

    Parameters:
    n (float): The number for which the floor value is computed.

    Returns:
    int: The floor value of the input float.
    """
    return math.floor(n)
