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

source1 = List()
source2 = List()
target = List()

source1_values = input(
    "Enter values for source 1 seperated by spaces: ").split()

for i in source1_values:
    source1.append(int(i))

print("Source 1 elements:", end=" ")
for value in source1:
    print(value, end=" ")

print()

source2_values = input(
    "Enter values for source 2 seperated by spaces: ").split()

for i in source2_values:
    source2.append(int(i))

print("Source 2 elements:", end=" ")
for value in source2:
    print(value, end=" ")

print()
