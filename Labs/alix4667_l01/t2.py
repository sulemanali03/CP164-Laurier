"""
-------------------------------------------------------
CP164 Lab 01, Testing
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
# Constants

movie = Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8])
print(movie, end='')
print(movie.genres_list_string)
