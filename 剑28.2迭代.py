class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self,root):
        if root is None:
            return True
        q = []
        q.append(root.left)
        q.append(root.right)
        while len(q) != 0:
            A = q.pop(0)
            B = q.pop(0)
            if A == None and B == None:
                continue
            if A == None or B == None:
                return False
            if A.val != B.val:
                return False
            q.append(A.left)
            q.append(B.right)
            q.append(A.right)
            q.append(B/left)
        return True
