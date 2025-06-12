

#Accessing / Traversing List

shopping=['Milk','Bread','Burger']

print("Milk" in shopping)
print(shopping[2])
shopping[0]='text add'

for i in shopping:
    print(i)

def shoppings(lists):
    for i in range(len(lists)):
        print(i,lists[i])

shoppings(shopping)


shopping.append('cow')
print(shopping)

shopping.insert(2,'add insrt')
print(shopping)

new=['mobail','tab','leptop']
shopping.extend(new)
print(shopping)

shopping.sort()
print(shopping)

shopping.reverse()
print(shopping)