"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-23"
-------------------------------------------------------
"""
# Imports

from Stack_array import Stack
from utilities import array_to_stack, stack_to_array


# Constants

stack = Stack()

source = ["First", "top", "middle", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)
