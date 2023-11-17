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
from Queue_array import Queue
# Constants
source1 = Queue()
source2 = Queue()

# Populate source1 and source2
source1._values = [5, 8, 12, 8]
source2._values = [7, 9, 14]

# Create a target queue and combine source1 and source2 into it
target = Queue()
target.combine(source1, source2)

# Print the results
print("source1:", source1._values)
print("source2:", source2._values)
print("target:", target._values)
