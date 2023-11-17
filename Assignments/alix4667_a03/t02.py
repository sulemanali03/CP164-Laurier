"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-01"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants

source = Stack()
values = [8, 14, 12, 9, 8, 7, 5]

for value in values:
    source.push(value)

target1, target2 = source.split_alt()

print("source:", source._values)
print("target1:", target1._values)
print("target2:", target2._values)
