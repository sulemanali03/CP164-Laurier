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
from functions import stack_reverse

stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

stack_reverse(stack)

for i in stack:
    print(i)
