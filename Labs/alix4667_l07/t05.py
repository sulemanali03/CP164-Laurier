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

lst1 = List()

values1 = input("Enter values for list 1 seperated by spaces: ").split()

for i in values1:
    lst1.append(int(i))

print("List 1 elements:", end=" ")
for value in lst1:
    print(value, end=" ")

print()

lst2 = List()

values2 = input("Enter values for list 2 seperated by spaces: ").split()

for i in values2:
    lst2.append(int(i))

print("List 2 elements:", end=" ")
for value in lst2:
    print(value, end=" ")

print()
