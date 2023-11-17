"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-11-12"
-------------------------------------------------------
"""
# Imports
from morse import ByLetter

one = ByLetter("A", ",-")
oneagain = ByLetter("A", ",-")
two = ByLetter("B", "-...")

print(one == two)
print(one < two)
print(one <= oneagain)
print(two)
