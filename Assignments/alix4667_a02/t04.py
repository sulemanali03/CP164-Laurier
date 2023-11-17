"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-24"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import read_movies, get_by_genres

# Constants
file = open('movies.txt', "rt")

movies = read_movies(file)

file.close()

gmovies = get_by_genres(movies, [3, 4])

for movie in gmovies:
    print(movie, end="\n\n")
