
# search list

my_list=[10,20,30,40,50,60,70,80,90]
print(len(my_list))
print(max(my_list))
print(sum(my_list))
print(sum(my_list)/len(my_list))


target=20

# if target in my_list:
#     print(f"{target} is this list")
# else:
#     print(f"{target} is not list")

#linear search

def linear_search(p_list,p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(my_list,target))
