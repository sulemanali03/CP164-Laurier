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
from Priority_Queue_array import Priority_Queue

# Constants


pq = Priority_Queue()

value = int(input("Enter a number: "))

pq.insert(value)

print(pq.peek())
