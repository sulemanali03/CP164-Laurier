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
from List_array import List
from Movie_utilities import read_movies
from Movie import Movie

l1 = List()
l2 = List()
l3 = List()
l4 = List()
l5 = List()
l3._values = [1, 3, 5, 6, 3, 5, 6, 1]
key = Movie('Fake Movie', 2015, None, None, None)

fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close
for f in movies:
    l1.append(f)

fv2 = open("movies2.txt", "r", encoding="utf-8")
movies2 = read_movies(fv2)
fv2.close
for j in movies2:
    l2.append(j)

fv3 = open("movies3.txt", "r", encoding="utf-8")
movies3 = read_movies(fv3)
fv3.close

equals = l1 == l2
print(f"__eq__: {equals}\n")

print(f"__getitem__:\n{l1.__getitem__(3)}\n")

l3.clean()
print(f"Clean: {l3._values}\n")

l4.combine(l1, l2)
print("Combine:")
for i in l4:
    print(f"{i}\n")

print(f"l1 and l2 after combine: {l1._values},{l2._values}\n")

for f in movies:
    l1.append(f)
for j in movies2:
    l2.append(j)

l5.intersection(l1, l2)
print("Intersection:")
for f in l5:
    print(f"{f}\n")

l3.prepend(1)
print(l3._values)

l3.remove_front()
print(l3._values)

l2.remove_many(key)
print("\nRemove Many:")
for i in l2:
    print(f"{i}\n")

list_movies_splitting = List()
for i in movies3:
    list_movies_splitting.append(i)

l6, l7 = list_movies_splitting.split_alt()
print("split_alt:")
print("First list:")
for f in l6:
    print(f"{f}\n")
print("Second list:")
for f in l7:
    print(f"{f}\n")

l8 = List()
for w in range(15):
    l8.append(w)

l9 = List()
l9.union(l3, l8)
print("Union:")
print(l9._values)
