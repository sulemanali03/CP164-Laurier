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
from Sorts_array import Sorts


print("Array before radix sort: ")
arr = [78, 89, 58, 7, 89, 90, 224, 567, 65]
print(arr)
Sorts.radix_sort(arr)
print("\nArray after radix sort: ")
print(arr)
