class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)
        else:
            print("Value already exists in the tree.")

    def traverse_inorder(self):
        if self.root is not None:
            self._traverse_inorder_recursive(self.root)

    def _traverse_inorder_recursive(self, current_node):
        if current_node is not None:
            self._traverse_inorder_recursive(current_node.left)
            print(current_node.value, end=" ")
            self._traverse_inorder_recursive(current_node.right)


tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)

tree.traverse_inorder()  # Output: 1 3 4 5 8
