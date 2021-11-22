class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self,root):
        
        def dfs(node,level):
            if level == len(res):
                res.append(node.val)
            for child in (node.right,node.left):
                if child:
                    dfs(child,level+1)
        if not root:
            return []
        res = []
        dfs(root,0)
        return res
    
