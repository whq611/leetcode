class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self,root):
        if not root:
            return []
        next_level = [root]
        res = []
        while next_level:
            cur_level = next_level
            next_level = []
            while cur_level:
                node = cur.level.pop()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(node.val)
        return res
