'''
What is an Array?

An array in Python (via the array module) stores elements
of the same data type efficiently but has limited functionality.

A NumPy array (ndarray) is more powerful, supporting:
- Multi-dimensional data
- Broadcasting
- Vectorized operations
- Mathematical functions

It is ideal for scientific computing and data analysis.
'''

'''
Why Do We Need Arrays?

Arrays help store multiple values of the same type in a single variable.
They:
- Use less memory
- Allow fast access
- Support mathematical and logical operations

Especially useful in data processing and numerical computing.
'''

'''
Two Types of Arrays: Single-Dimensional and Multi-Dimensional
'''

import numpy as np  # Import NumPy library for array operations

# ------------------- 1D ARRAY -------------------
# Creating a 1D NumPy array (like a simple list of values)
arr_1d = np.array([10, 20, 30, 40])

# Printing the 1D array
print("1D Array:", arr_1d)

# Accessing the second element (indexing starts at 0)
print("Second element of 1D array:", arr_1d[1])


# ------------------- 2D ARRAY -------------------
# Creating a 2D NumPy array (matrix with rows and columns)
arr_2d = np.array([
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
])

# Printing the entire 2D array
print("\n2D Array:\n", arr_2d)

# Accessing an element at row 1, column 2 (indexes start at 0)
print("Element at (1, 2):", arr_2d[1, 2])  # Output: 6

# Getting the shape of the array (rows, columns)
print("Shape of 2D array:", arr_2d.shape)

# Looping through each row of the 2D array
print("\nRows in 2D array:")
for row in arr_2d:
    print(row)


'''
📌 One-Dimensional vs Two-Dimensional Memory

🔹 1D Memory (One-Dimensional)
    - Data is stored in a single line (linear format)
    - Example: [10, 20, 30, 40]
    - Like a row or a simple list
    - Access with one index: arr[2] → 30

🔹 2D Memory (Two-Dimensional)
    - Data stored in rows and columns (matrix format)
    - Example:
        [
          [1, 2, 3],
          [4, 5, 6]
        ]
    - Access with two indices: arr[1][2] → 6
    - Used for tables, images, spreadsheets, etc.

🧠 Internally in memory:
    - 1D: Stored in a single block (contiguous)
    - 2D: Stored as array of arrays (row-major or column-major order)


'''
