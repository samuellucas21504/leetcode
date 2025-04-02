class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        pass

    def add_to_tail(self, value):
        node = Node(value)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        pass

    def pop_head(self):
        if not self.head:
            return None

        removed_node = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return removed_node

    def pop_tail(self):
        if not self.tail:
            return None

        removed_node = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed_node

# Creating the list
dll = DoublyLinkedList()
# []

# Adding elements to the head
dll.add_to_head(10)
dll.add_to_head(20)
dll.add_to_head(30)
# [ 30, 20, 10 ]

# Displaying values
print(dll.head.value)  # Should be 30
print(dll.head.next.value)  # Should be 20
print(dll.head.next.next.value)  # Should be 10

# Adding elements to the tail
dll.add_to_tail(5)
dll.add_to_tail(0)
# [ 30, 20, 10, 5, 0 ]

# Displaying values
print(dll.tail.value)  # Should be 0
print(dll.tail.prev.value)  # Should be 5

# Removing from the head
print(dll.pop_head())  # Should be 30
print(dll.pop_head())  # Should be 20
# [ 10, 5, 0 ]

# Removing from the tail
print(dll.pop_tail())  # Should be 0
print(dll.pop_tail())  # Should be 5
print(dll.pop_tail())  # Should be 10
# []

# Checking if the list is empty
print(dll.pop_head())  # Should be None
print(dll.pop_tail())  # Should be None
