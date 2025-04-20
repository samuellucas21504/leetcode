class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, key):
        if key in self.cache:
            node = self.cache[key]
            node.prev.next, node.next.prev = node.next, node.prev
            self.cache.pop(key)

    def add_to_end(self, node: Node):
        node.prev, node.next = self.right.prev, self.right
        self.right.prev.next, self.right.prev = node, node

    def move_to_end(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.add_to_end(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        node = Node(key, value)
        self.add_to_end(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru.key)
