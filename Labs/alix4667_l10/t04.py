"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from test_Sorts_List_linked import test_sort, SORTS

header1 = "n:   100               |      Comparisons       | |         Swaps          |"
header2 = "Algorithm              In Order Reversed   Random In Order Reversed   Random"
header3 = "--------------         -------- -------- -------- -------- -------- --------"

print(header1)
print(header2)
print(header3)
for i in SORTS:
    test_sort(i[0], i[1])
