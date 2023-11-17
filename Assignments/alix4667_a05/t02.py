"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies
from Movie import Movie

l1 = Sorted_List()
l2 = Sorted_List()
l3 = Sorted_List()
l4 = Sorted_List()
for f in range(10):
    l1.insert(f)
print(f"l1: {l1._values})")
print(f"Max: {l1.max()}")
print(f"Min: {l1.min()}")
for f in range(5):
    l1.insert(10)
print(f"Count: {l1.count(10)}")
print(f"Contains: {l1.__contains__(10)}, {l1.__contains__(15)}")
print(f"Get Item: {l1.__getitem__(11)}")
l2 = Sorted_List()
print(f"__eq__: {l1.__eq__(l2)}")
print(f"Clean:")
l1.clean()
print(l1._values)

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close

fv2 = open("movies2.txt", "r", encoding="utf-8")
movies2 = read_movies(fv2)
fv.close

fv3 = open("movies3.txt", "r", encoding="utf-8")
movies3 = read_movies(fv3)
fv.close

for f in movies:
    l2.insert(f)
for q in movies2:
    l3.insert(q)

key = Movie('Fake Movie', 2015, None, None, None)
print(f"\nFind\n{l2.find(key)}")
print(f"\nIndex\n{l2.index(key)}")
l4.intersection(l2, l3)
print(f"\nIntersection")
for p in l4:
    print(f"{f}\n")
print(f"Peek:\n{l2.peek()}")
print(f"\nRemove:\n{l3.remove(key)}")
print(f"\nRemove Front:\n{l2.remove_front()}")
print("\nRemove many\n")
l3.remove_many(key)
for i in l3:
    print(f"{i}\n")
print("Union\n")
l4.union(l2, l3)
for i in l4:
    print(f"{i}\n")
print("Split Key\n")
l5, l6 = l3.split_key(key)
l7, l8 = l4.split_alt()
