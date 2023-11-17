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
from morse import decode_morse
from BST_linked import BST
from morse import fill_code_bst
from morse import DATA1

s = BST()
morse_data = DATA1
fill_code_bst(s, morse_data)


text_to_decode = "-  .-  -  .-  -.-  .-  ."

decoded_text = decode_morse(s, text_to_decode)
print(decoded_text)
