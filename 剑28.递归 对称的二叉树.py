class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self,root):
        def recur(l,r):
            if not l and not r:
                return True
            elif (not l and r) or (not r and l) or (l.val != r.val):
                return False
            else:
                return recur(l.left,r.right) and recur(l.right,r.left)
        if not root:
            return True
        else:
            return recur(root.left,root.right)
