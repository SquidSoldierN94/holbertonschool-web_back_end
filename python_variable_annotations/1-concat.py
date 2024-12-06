#!/usr/bin/env python3

"""
This module contains a function `concat` that takes two string values 
as arguments and returns their concatenation as a single string. 
This module demonstrates type annotations for string operations in Python.
"""

def concat(str1: str, str2: str) -> str:
    """
    Concatenates two string arguments and returns the resulting string.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: The concatenated result of str1 and str2.
    """
    return str1 + str2
