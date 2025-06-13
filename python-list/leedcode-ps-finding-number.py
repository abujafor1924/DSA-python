
import numpy as np

my_array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def find_number(array,number):
    for i in range(len(array)):
        if array[i]== number:
            print(i)
        


find_number(my_array,12)