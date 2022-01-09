class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        a = [root]
        ans = []
        while a:
            b = a.pop(0)
            ans.append(b.val)
            if b.left:
                a.append(b.left)
            if b.right:
                a.append(b.right)
        return ans
