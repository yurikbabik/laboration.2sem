class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode) -> int:
    if not root:
        raise ValueError("дерево не може бути пустим")

    def calculate_depth(node, depth):
        if not node:
            return 0
        return depth + calculate_depth(node.left, depth + 1) + calculate_depth(node.right, depth + 1)

    return calculate_depth(root, 0)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

print(sum_of_depths(root))

