"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

hset = Hash_Set(5)
for i in range(8):
    hset.insert(i)

print("Before rehashing:")
hset.debug()

hset._rehash()

print("\nAfter rehashing:")
hset.debug()
