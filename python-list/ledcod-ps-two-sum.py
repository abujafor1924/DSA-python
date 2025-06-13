
def findPires(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]==num[j]:
                continue
            elif num[i]+num[j] == target:
                print(i,j)

my_list=[1,2,3,4,5,6,7,8,9]
findPires(my_list,6)