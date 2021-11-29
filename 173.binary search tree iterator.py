class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self,root):
        self.nodes_sorted = []
        self.index = -1
        self.inorder(root)
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.nodes_sorted.append(root.val)
        self.inorder(root.right)
    def next(self):
        self.index += 1
        return self.nodes_sorted[self.index]
    def hasnext(self):
        return self.index+1 < len(self.nodes_sorted)
