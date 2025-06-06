import numpy as np

to_DArray = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [15, 17, 18, 19]
])
print(to_DArray)

print("insert array 2/3 D Array")

new_twoD_array=np.insert(to_DArray,0,[[20,21,22,23]],axis=0)
print(new_twoD_array)

print("accesing two D  array")
print(new_twoD_array[1][2])

print("access element by functions")
def accessElement(arr,rowIndex,colindex):
    if rowIndex >= len(arr) and colindex>=len(arr):
        print("Incorrect Index")
    else:
        print(arr[rowIndex][colindex])

accessElement(new_twoD_array,2,2)