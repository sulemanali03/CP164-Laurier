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
from functions import median_scores
# Constants

with open("numbers.txt", "r") as file:
    result = median_scores(file)

print(f"Median score: {result}")
