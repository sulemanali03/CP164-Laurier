"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports

# Constants

from Queue_circular import Queue


target = Queue()
target.insert(1)
target.insert(2)
target.remove()

source = Queue()
source.insert(2)


equals = source == target

print(equals)
