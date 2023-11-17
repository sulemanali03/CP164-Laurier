"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-11-12"
-------------------------------------------------------
"""
# Imports
from morse import fill_letter_bst
from BST_linked import BST


s = BST()

fill_letter_bst(s, (['A', '.-'], ['B', '-...']))
print(s._root)
