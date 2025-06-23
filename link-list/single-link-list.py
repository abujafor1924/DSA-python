
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

new_linklist=LinkList(10)
print(new_linklist)
print(new_linklist.head)
print(new_linklist.tail)
