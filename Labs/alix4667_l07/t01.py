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

values = input("Enter a list of integers separated by spaces: ").split()

for i in values:
    lst.append(int(i))

print("List elements:", end=" ")
for value in lst:
    print(value, end=" ")

print()
key = int(input("Enter an integer key to search for: "))

previous, current, index = lst._linear_search_r_aux(key, None, lst._front, 0)

if index == -1:
    print(f"The key {key} was not found in the list.")
else:
    print(f"The key {key} was found at index {index}.")
