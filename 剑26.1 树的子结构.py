class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self,A,B):
        if not A or not B:
            return False
        def recur(A,B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left,B.left) and recur(A.right,B.right)
        return recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStruture(A.right,B)
