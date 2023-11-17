"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants

from Movie_utilities import read_movies
from utilities import list_test

file = open("movies.txt", "rt")

source = read_movies(file)

file.close()

list_test(source)
