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

# Constants

from Hash_Set_BST import Hash_Set

from functions import insert_words, comparison_total

hs = Hash_Set(20)

fv = open("miserables.txt", "r")


insert_words(fv, hs)

total, max_word = comparison_total(hs)

print(f"Using array-based list Hash_Set")
print(f"Total Comparisons:{total}")
print(
    f"Word with maximum comparisons '{max_word.word}', {max_word.comparisons}")

fv.close()
