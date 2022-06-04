class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(left,right):
            if not left and not right:
                return True
            if (left and not right) or (right and not left):
                return False
            if left.val != right.val:
                return False
            return helper(left.left,right.right) and helper(left.right,right.left)
        return helper(root.left, root.right)
