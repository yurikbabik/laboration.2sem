import unittest
from lab3 import TreeNode, sum_of_depths

class TestSumOfDepths(unittest.TestCase):
    def test_example_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(sum_of_depths(root), 6)

    def test_single_node(self):
        root = TreeNode(10)
        self.assertEqual(sum_of_depths(root), 0)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(sum_of_depths(root), 3)




if __name__ == '__main__':
    unittest.main()
