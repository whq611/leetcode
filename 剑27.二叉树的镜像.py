# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root):
        if not root:
            return None
        root2 = TreeNode(root.val)
        def helper(node1,node2):
            if node1.left:
                node2.right = TreeNode(node1.left.val)
                helper(node1.left,node2.right)
            if node1.right:
                node2.left = TreeNode(node1.right.val)
                helper(node1.right,node2.left)
        helper(root,root2)
        return root2
