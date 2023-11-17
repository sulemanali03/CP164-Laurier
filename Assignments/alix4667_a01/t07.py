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
from functions import matrix_transpose

# Constants

test_matrix = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
result = matrix_transpose(test_matrix)

for row in result:
    print(row)
