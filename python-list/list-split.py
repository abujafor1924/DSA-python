
a='spam spam spam'

print('list')
b=list(a)
print(b)

print('split')
b=a.split()
print(b)

print('delimiter')
a='spam-spam1-spam2'
delimiter="-"
b=a.split(delimiter)
print(b)
#added again
print(delimiter.join(b))