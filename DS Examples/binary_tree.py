class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node: Node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursively(self.root, data)

    def _search_recursively(self, node: Node, data):
        if node is None:
            return False

        if data == node.data:
            return True

        if data < node.data:
            node_to_search = node.left
        else:
            node_to_search = node.right

        return self._search_recursively(node_to_search, data)

    def preoder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)

print(tree.preoder_traversal())
print(tree.inorder_traversal())
print(tree.postorder_traversal())

print("Search 4:", tree.search(4))
print("Search 6:", tree.search(6))
print("Search 8:", tree.search(8))
