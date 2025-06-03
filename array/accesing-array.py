
from array import  *

arr=array('i',[1,2,3,4,5,6,7,8,9])

def accessing_array(array,index):
    if index>len(array):
        print("There are No element in array")
    else:
        print(array[index])



accessing_array(arr,1)


def searching_array(array,target):
    for i in range(len(array)):
        if array[i]== target:
            return i
    return "Dosn't match Any index"

my_array=searching_array(arr,1)
print(my_array)


