"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-11-19"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import letter_table, insert_test, do_comparisons

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
insert_test(bst1, DATA1)

fv = open("miserables.txt", "r")
do_comparisons(fv, bst1)

letter_table(bst1)
fv.close()
