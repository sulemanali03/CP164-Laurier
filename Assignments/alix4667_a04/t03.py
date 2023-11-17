"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
# Imports
from functions import queue_combine
from Queue_array import Queue
# Constants

source1 = Queue()
source1.insert(5)
source1.insert(8)
source1.insert(12)
source1.insert(8)

source2 = Queue()
source2.insert(7)
source2.insert(9)
source2.insert(14)

target = queue_combine(source1, source2)

print("source1:", end=" ")
while not source1.is_empty():
    print(source1.remove(), end=", ")

print("\nsource2:", end=" ")
while not source2.is_empty():
    print(source2.remove(), end=", ")

print("\ntarget:", end=" ")
while not target.is_empty():
    print(target.remove(), end=", ")
