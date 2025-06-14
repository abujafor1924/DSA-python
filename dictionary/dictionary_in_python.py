

my_dict=dict()
print(my_dict)
my_dict2={}
print(my_dict2)

eng_sp=dict(one="uno",two="dos",three="tres")
print(eng_sp)

eng_sp1={'one':"uno",'two':"dos",'three':"tres"}
print(eng_sp1)

eng_sp_list=[('one',"uno"),('two',"dos"),('three',"tres")]
eng_sp2=dict(eng_sp_list)
print(eng_sp2)

my_bio={'name':'akil','age':23}
my_bio['age']=27
my_bio['address']='london'
print(my_bio)



my_bio_sec={'name':"akil",'age':23,'address':"london"}

def traversing(dict):
    for i in dict:
        # print(i) # only value
        print(i,dict[i])
traversing(my_bio_sec)

print("search value")

my_bio_the={'name':"akil",'age':23,'address':"london"}

def searchDict(dict,value):
    for i in dict:
        if dict[i]==value:
            return i,value
    return "the value dosn't exist"

print(searchDict(my_bio_the,23))
