
print("Bog o Notation.")

# Big-O 1
def sum(a,t):
    print(a+t)
sum(3,3)

# Big-O n

def print_item(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_item(10)

# Big-O n^2
def print_item(n):
    for i in range(n):
       for j in range(n):
        print(i,j)

print_item(10)


'''
Time Complexity: O(n)
There are two separate loops, but not nested.

Each loop runs n times.

So, total operations = n + n = 2n.

In Big-O notation, we drop constants → O(n).

--------------------------------------- o n^2 ----------------------
Time Complexity: O(n²)
This time, the loops are nested.

For every i, the inner loop runs n times.

So total operations = n × n = n² → O(n²)
======================================
Simple Analogy
Imagine you're checking every student in a class:

O(n): You go through the students one by one — simple roll call.

O(n²): You check every student with every other student — like forming all pairs or comparing everyone.
'''


# big-O log-n


'''
Why is this O(log n)?
Each time, the search space is cut in half.

If the list has n elements:

First step: search n elements

Second step: search n/2 elements

Third step: n/4 elements

...

This continues until 1 element is left.

This "divide in half" process is what gives it a logarithmic time complexity:
O(log n)



'''

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(arr, 13))  # Output: 6
