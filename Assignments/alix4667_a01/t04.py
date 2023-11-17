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
from functions import is_palindrome

# Constants

s = input("Enter: ")

palindrome = is_palindrome(s)

if palindrome:
    print(f"{s} is a palindrome")
else:
    print(f'{s} is not a palindrome')
