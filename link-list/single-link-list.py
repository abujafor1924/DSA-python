# Node class represents each element in the linked list
class Node:
    def __init__(self, value):
        self.value = value      # Stores the value of the node
        self.next = None        # Pointer to the next node (initially None)


# Linked List class to manage the entire list
class LinkList:
    def __init__(self, value):
        new_node = Node(value)   # Create the first node
        self.head = new_node     # Head points to the first node
        self.tail = new_node     # Tail also points to the same node
        self.length = 1          # List starts with one node

    # Add a new node at the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:         # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link old tail to new node
            self.tail = new_node       # Update tail
        self.length += 1

    # Add a new node at the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:         # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Point new node to old head
            self.head = new_node       # Update head
        self.length += 1

    # Insert a node at a specific index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False  # Invalid index

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):     # Traverse to the node before index
            temp_node = temp_node.next

        new_node.next = temp_node.next  # Connect new node to the next node
        temp_node.next = new_node       # Connect previous node to new node
        self.length += 1
        return True

    # Traverse through the list and print each value on a new line
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    # Search for a value in the list
    def search(self, target):
        current_node = self.head
        while current_node is not None:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False

    # String representation: e.g. 5->10->15->20->30
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result


# ✅ Testing the Linked List

# Create a new linked list with the first node value 10
new_linklist = LinkList(10)

# Append 20 and 30 to the end of the list
new_linklist.append(20)
new_linklist.append(30)

# Prepend 5 to the beginning of the list
new_linklist.prepend(5)

# Insert 15 at index 2 (between 10 and 20)
success = new_linklist.insert(2, 15)
print("Insert status:", success)  # Output: True

# Try inserting at an invalid index
fail = new_linklist.insert(10, 99)
print("Insert status (invalid index):", fail)  # Output: False

# Print the entire list using __str__
print("Linked List:", new_linklist)  # Output: 5->10->15->20->30

# Print all node values one by one
print("\nTraverse each value:")
new_linklist.traverse()

# Print head and tail values
print("\nHead:", new_linklist.head.value)   # Output: 5
print("Tail:", new_linklist.tail.value)     # Output: 30

# Print the length of the list
print("Length:", new_linklist.length)       # Output: 5

# ✅ Search test
print("\nSearch for 15:", new_linklist.search(15))  # Output: True
print("Search for 99:", new_linklist.search(99))    # Output: False
