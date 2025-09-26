#!/usr/bin/env python3
# Author: Arib Noor
# Date: Sept 26 2025
# Purpose: Create Simple Functions.
# Usage: ./lab3f.py

"""
Write a function that takes a list as argument and return true if any number in the list is even, the function returns false otherwise.
Call the function with a list of 6 integer values.
"""
# TO DO 1: Add the docstring
def isAnyEven(list):
    """
    @Function definition: checks if any integer in a list is true
    @param: list: a list of integers
    @return: boolean: true if any integer in list is even, otherwise returns false
    """
    for i in list:
        if i % 2 == 0:
            return True
    return False
        
list = [1,2,3,4,5,6]
print(isAnyEven(list))