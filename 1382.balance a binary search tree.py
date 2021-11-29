class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self,root):
        def getInorder(node):
            if node:
                getInorder(node.left)
                inorderSeq.append(node.val)
                getInorder(node.right)
        def build(l,r):
            m=(l+r)//2
            node = TreeNode(inorderSeq[m])
            if l<=m-1:
                node.left = build(l,m-1)
            if r>=m+1:
                node.right = build(r,m+1)
            return node
        inorderSeq = []
        getInorder(root)
        return build(0,len(inorderSeq)-1)
