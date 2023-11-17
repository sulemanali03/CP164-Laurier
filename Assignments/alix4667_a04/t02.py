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

from Queue_array import Queue

queue1 = Queue()
queue2 = Queue()

queue1.insert(1)
queue1.insert(2)
queue1.insert(3)

queue2.insert(1)
queue2.insert(2)
queue2.insert(4)

if queue1 == queue2:
    print("Queues are equal.")
else:
    print("Queues are not equal.")
