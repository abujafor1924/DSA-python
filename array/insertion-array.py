import array

# Create an array of integers
arr = array.array('i', [1, 2, 4, 5])

# Use insert() to add 3 at index 2
arr.insert(2, 3)

print(arr.tolist())
# Output: [1, 2, 3, 4, 5]


import numpy as np

arr = np.array([1, 2, 4, 5])

# Insert 3 at index 2
new_arr = np.insert(arr, 2, 3)

print(new_arr)
# Output: [1 2 3 4 5]
