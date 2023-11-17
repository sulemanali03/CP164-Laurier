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
from Movie_utilities import read_movies, genre_counts

# Constants
file = open('movies.txt', "rt")

movies = read_movies(file)

file.close()

counts = genre_counts(movies)

for i, count in enumerate(counts):
    print(f"{Movie.GENRES[i]}: {count}")
