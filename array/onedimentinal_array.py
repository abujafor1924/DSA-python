
from array import *

my_array=array('i',[1,2,3,4,5,6,7,8,9])

print("step-1")
for i in my_array:
    print(i)


print("step-2")
print(my_array[2])

print("step-3")
my_array.append(10)
print(my_array)

print("step-4")
my_array.insert(10,11)
print(my_array)

print("step-5")
arr1=array('i',[12,13,14])
my_array.extend(arr1)
print(arr1)

print("step-6")
templist=[20,21,22]
my_array.fromlist(templist)
print(my_array)

print("step-7")
my_array.remove(21)
print(my_array)

print("step-8")
my_array.pop()
print(my_array)

print("step-9")
i=my_array.index(20)
print(i)

print("step-10")
my_array.reverse()
print(my_array)

print("step-11")
b=my_array.buffer_info()
print(b)

print("step-12")
c=my_array.count(11)
print(c)

print("step-13")
s=my_array.tostring()
print(s)

print("step-14")
print(my_array[2:])
print(my_array[1:4])