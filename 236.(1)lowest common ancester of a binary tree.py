class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        def recurse_tree(self,current_node):
            if not current_node:
                return None
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q

            if left+right+mid >= 2:
                self.res = current_node
            return left or right or mid
        recurse_tree(root)

        return self.res
