"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-23"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from utilities import stack_test
# Constants

file = open('movies.txt', "rt")

movies = read_movies(file)

file.close()

stack_test(movies)
