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
from functions import do_comparisons, comparison_total, insert_test

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

insert_test(bst1, DATA1)
insert_test(bst2, DATA2)
insert_test(bst3, DATA3)

fv = open("miserables.txt", "r")
do_comparisons(fv, bst1)
print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"Total Comparisons: {comparison_total(bst1):,}")
print("----------------------------------------------")
fv.close()

fv = open("miserables.txt", "r")
do_comparisons(fv, bst2)
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print(f"Total Comparisons: {comparison_total(bst2):,}")
print("----------------------------------------------")
fv.close()


fv = open("miserables.txt", "r")
do_comparisons(fv, bst3)
