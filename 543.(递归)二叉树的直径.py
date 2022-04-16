class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def max_depth(root):
            if not root:
                return 0
            max_left = max_depth(root.left)
            max_right = max_depth(root.right)
            self.res = max(self.res,max_left+max_right+1)
            return max(max_left,max_right)+1
        max_depth(root)
        return self.res-1
