class Node:
    def __init__(self, value, priority, left = None, right = None ):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right

class Priority:
    def __init__(self, root = None ):
        self.root = root

    def insert(self, value, priority):
        def _insert(node, value, priority):
            if node is None:
                return Node(value, priority)
            if priority > node.priority:
                node.left = _insert(node.left, value, priority)
            if priority <=node.priority:
                node.right = _insert(node.right, value, priority)
            return node

        self.root = _insert(self.root, value, priority)

    def find_max(self, node):
        if node is None:
            return None, None
        if node.left is None:
            return node, None
        parent = None
        while node.left:
            parent = node
            node = node.left
        return node, parent

    def remove_max(self):
        if self.root is None:
            return None
        max_node, parent = self.find_max(self.root)
        if parent is None:
            self.root = self.root.right
        else:
            parent.left = max_node.right
        return max_node.value

    def peek_max(self):
        node = self.root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.value

