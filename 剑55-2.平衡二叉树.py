class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self,root):
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1
        if not root:
            return True
        return abs(height(root.left)-height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
