class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isBST(self, root):
        # Helper function with min and max range
        def is_valid(node, min_val, max_val):
            if node is None:
                return True
            if not (min_val < node.data < max_val):
                return False
            return (is_valid(node.left, min_val, node.data) and
                    is_valid(node.right, node.data, max_val))

        return is_valid(root, float('-inf'), float('inf'))
