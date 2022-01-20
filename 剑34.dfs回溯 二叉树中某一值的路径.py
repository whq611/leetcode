# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, target):
        def dfs(node,s,tmp):
            if not node:
                return
            tmp.append(node.val)
            if not node.left and not node.right and s+node.val == target:
                res.append(list(tmp))                
            dfs(node.left,s+node.val,tmp)
            dfs(node.right,s+node.val,tmp)
            tmp.pop()
        res = []
        dfs(root,0,[])
        return res
