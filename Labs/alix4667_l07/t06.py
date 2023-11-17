"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-11-05"
-------------------------------------------------------
"""
# Imports

# Constants

from List_linked import List

lst = List()

values = input("Enter values for list seperated by spaces: ").split()

for i in values:
    lst.append(int(i))

print("List elements:", end=" ")
for value in lst:
    print(value, end=" ")

lst.reverse_r()

print()
print("Reversed list elements:", end=" ")
for value in lst:
    print(value, end=" ")
