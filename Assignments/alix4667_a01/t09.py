"""
-------------------------------------------------------
CP164 Assignment 01, Testing
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports
from functions import matrix_rotate_right

# Constants

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
result = matrix_rotate_right(matrix_a)

for row in result:
    print(row)
