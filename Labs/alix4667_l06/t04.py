"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-26"
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

for value in movies:
    new_list.append(value)

print(new_list.count(movies[5]))

print()
print(new_list.max())

print()
print(new_list.min())
