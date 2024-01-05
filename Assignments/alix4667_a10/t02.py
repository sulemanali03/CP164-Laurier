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
from List_linked import List
from Sorts_List_linked import Sorts


arr = [12, 43, 65, 98, 57, 4, 8, 25, 33, 41]

lst = List()

for val in arr:
    lst.append(val)

print("List before radix sort: ")
for i in lst:
    print(i)

Sorts.radix_sort(lst)

print("\nList after radix sort: ")
for i in lst:
    print(i)
