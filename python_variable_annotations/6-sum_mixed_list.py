#!/usr/bin/env python3
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all the elements in a list of integers and floats.

    This function takes a list containing both integers and floating-point numbers
    and returns their sum as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and/or floats to sum.

    Returns:
    float: The sum of all the numbers in the input list, represented as a float.
    """
    return float(sum(mxd_lst))
