"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

# Constants


queue = Queue()

insert_value = input("Enter a value: ")

queue.insert(insert_value)

print(queue.peek())

value = queue.remove()

print(value)
