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
from Movie_utilities import read_movies, get_by_rating


# Constants
file = open('movies.txt', "rt")

movies = read_movies(file)

file.close()

rmovies = get_by_rating(movies, 7.1)


for movie in rmovies:
    print(movie, end="\n\n")
