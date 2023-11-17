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
from functions import is_leap_year

# Constants

test_years = [1996, 2000, 2004, 1899, 1900, 1901, 1700, 1800, 1900, 1600, 2000]

for year in test_years:
    result = is_leap_year(year)
    print(f"{year} is a leap year: {result}")
