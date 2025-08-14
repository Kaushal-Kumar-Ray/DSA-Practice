class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        
        def isLeaf(node):
            return node.left is None and node.right is None
        
        def addLeftBoundary(node, res):
            curr = node.left
            while curr:
                if not isLeaf(curr):
                    res.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        
        def addLeaves(node, res):
            if isLeaf(node):
                res.append(node.data)
                return
            if node.left:
                addLeaves(node.left, res)
            if node.right:
                addLeaves(node.right, res)
        
        def addRightBoundary(node, res):
            curr = node.right
            temp = []
            while curr:
                if not isLeaf(curr):
                    temp.append(curr.data)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            res.extend(temp[::-1])
        
        res = []
        if not isLeaf(root):
            res.append(root.data)
        
        addLeftBoundary(root, res)
        addLeaves(root, res)
        addRightBoundary(root, res)
        
        return res


# Example usage
if __name__ == "__main__":
    # Tree: [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)

    sol = Solution()
    print(sol.boundaryTraversal(root))  # Output: [1, 2, 4, 8, 9, 6, 7, 3]
