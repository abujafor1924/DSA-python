class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

# পরীক্ষা
new_linklist = LinkList(10)
new_linklist.append(20)
new_linklist.append(30)

print(new_linklist)               # Output: 10->20->30
print(new_linklist.head.value)   # Output: 10
print(new_linklist.tail.value)   # Output: 30
