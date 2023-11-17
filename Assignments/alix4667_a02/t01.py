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
from Movie_utilities import read_movies, get_by_year

# Constants


file = open('movies.txt', "rt")

movies = read_movies(file)

file.close()

ymovies = get_by_year(movies, 1994)


for movie in ymovies:
    print(movie, end="\n\n")
