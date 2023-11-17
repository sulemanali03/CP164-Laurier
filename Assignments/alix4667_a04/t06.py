"""
-------------------------------------------------------
CP164
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
# Imports

# Constants


from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(5)
pq.insert(3)
pq.insert(8)
pq.insert(1)
pq.insert(7)

# Split the priority queue based on the key 4
target1, target2 = pq.split_key(4)

# Print the results
print("Values with priority > 4:", list(target1))  # [5, 8, 7]
print("Values with priority <= 4:", list(target2))
