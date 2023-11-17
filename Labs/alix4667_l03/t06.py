"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test

# Constants


pq = Priority_Queue()

source = [11, 22, 55, 44, 33]

array_to_pq(pq, source)

while len(pq) > 0:
    value = pq.remove()
    print(value)
    source.append(value)

array_to_pq(pq, source)

pq_to_array(pq, source)

print(source)

file_variable = open("movies.txt", "rt")

movies = read_movies(file_variable)

file_variable.close()

priority_queue_test(movies)
