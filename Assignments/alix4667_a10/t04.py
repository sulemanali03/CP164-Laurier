"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-12-04"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque


d = Deque()

arr = [12, 43, 65, 98, 57, 4, 8, 25, 33, 41]

for val in arr:
    d.insert_front(val)

print("Original Deque:")
for i in d:
    print(i)

Sorts.gnome_sort(d)

print("\nAfter Gnome Sort:")
for i in d:
    print (i)
