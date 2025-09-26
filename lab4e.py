#!/usr/bin/env python3
# Author: Arib Noor
# Date: Sept 26 2025
# Purpose: Create a matrix by two dimensional list.
# Usage: ./lab3e.py

# TO DO 1: Follow the instructions given in README.md file.
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

element = matrix[1][2]
# TO DO 2: Print the element 5 from list.
print(matrix[1][1])
# TO DO 3: Print the element 2 from list.
print(matrix[0][1])
# TO DO 4: Print the element 9 from list.
print(matrix[2][2])
# TO DO 5: Print individual lists from this matrix.
for l in matrix:
    print(l)
# TO DO 6: Print each individual element from the list.
for l in matrix:
    for e in l:
        print(e)