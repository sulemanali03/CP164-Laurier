"""
-------------------------------------------------------
CP164 Assignment 01, Testing
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""
# Imports
from functions import is_valid

# Constants

test_names = ["2var"]

for test_name in test_names:
    result = is_valid(test_name)
    print(result)
