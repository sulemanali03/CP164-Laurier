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
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

# Constants

queue = Queue()

source = [1, 2, 3]

array_to_queue(queue, source)

for _ in range(len(queue)):
    value = queue.remove()
    print(value)
    source.append(value)

array_to_queue(queue, source)

queue_to_array(queue, source)

print(source)

queue_test(source)
