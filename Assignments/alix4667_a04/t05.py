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
from functions import pq_split_key

pq = Priority_Queue()
pq.insert(10)
pq.insert(20)
pq.insert(5)
pq.insert(25)
pq.insert(15)

print("Original Priority Queue:")
while not pq.is_empty():
    print(pq.remove())

# Reset the Priority Queue
pq.insert(10)
pq.insert(20)
pq.insert(5)
pq.insert(25)
pq.insert(15)

# Split the Priority Queue
key = 15
target1, target2 = pq_split_key(pq, key)

print("\nPriority Queue with Priority > 15:")
while not target1.is_empty():
    print(target1.remove())

print("\nPriority Queue with Priority <= 15:")
while not target2.is_empty():
    print(target2.remove())
