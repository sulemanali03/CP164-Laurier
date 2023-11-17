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
from morse import encode_morse
from BST_linked import BST
from morse import fill_letter_bst
from morse import DATA1


s = BST()
morse_data = DATA1
fill_letter_bst(s, morse_data)


text_to_encode = "Tatakae!"


encoded_text = encode_morse(s, text_to_encode)


print(encoded_text)
