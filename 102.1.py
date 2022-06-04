class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node,level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left: helper(node.left,level+1)
            if node.right: helper(node.right,level+1)
        
        levels = []
        if not root:
            return levels
        helper(root,0)
        
        return levels
