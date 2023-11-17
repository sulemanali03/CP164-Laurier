"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack  # @UnusedImport
from utilities import array_to_stack
# Constants

stack = Stack()


source = ["top", "middle", "bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)
