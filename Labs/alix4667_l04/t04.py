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

from List_array import List

list1 = List()

list1.append(0)

list1.append(1)

list1.append(2)

list1.append(-1)

list1.append(-2)

print(list1.index(-1))

print(list1.find(-1))

if 2 in list1:
    print("2 is in list1")
else:
    print("Not in list1")

print(list1.count(0))

print(list1.min())

print(list1.max())
