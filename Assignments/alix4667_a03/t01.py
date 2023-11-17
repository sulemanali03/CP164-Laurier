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

# Constants
from Stack_array import Stack
from functions import stack_split_alt

source = Stack()
values = [8, 14, 12, 9, 8, 7, 5]

for value in values:
    source.push(value)

target1, target2 = stack_split_alt(source)

print("source:", end="\t")
while not source.is_empty():
    print(source.pop(), end=",")
print("\ntarget1:", end="\t")
while not target1.is_empty():
    print(target1.pop(), end=",")
print("\ntarget2:", end="\t")
while not target2.is_empty():
    print(target2.pop(), end=",")
