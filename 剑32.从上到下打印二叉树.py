class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self,root):
        def helper(node,level):
            if not node:
                return
            else:
                res[level].append(node.val)
                if len(res) == level + 1:
                    res.append([])
                helper(node.left,level+1)
                helper(node.right,level+1)
        res = [[]]
        helper(root,0)
        return res[:-1]
      
