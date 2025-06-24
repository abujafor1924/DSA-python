
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1


new_linklist=LinkList(10)
new_linklist.append(10)
new_linklist.append(20)

print(new_linklist)
print(new_linklist.head.value)
print(new_linklist.tail)
