"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports

# Constants

from Movie_utilities import read_movies
from List_linked import List

file_variable = open("movies.txt", "rt")

movies = read_movies(file_variable)

file_variable.close()

new_list = List()

new_list.append(movies[2])

new_list.prepend(movies[0])

new_list.insert(1, movies[1])

for value in new_list:
    print(value)
    print()
