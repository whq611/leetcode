class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def buildTree(self,preorder,inorder):
        def myBuildTree(preorder_left,preorder_right,inorder_left,inorder_right):
            if preorder_left>preorder_right:
                return None
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            root = TreeNonde(preorder[preorder_root])
            size_left_subtree = inorder_root-inorder_left
            root.left = myBuildTree(preorder_left+1,preorder_left+size_left_subtree,inorder_left,inorder_root-1)
            root.right = myBuildTree(preorder_left+size_left_subtree+1,preorder_right,inorder_root+1,inorder_right)
            return root

            


        n = len(preorder)
        index = {element:i for i,element in enumerate(inorder)}
        return myBuildTree(0,n-1,0,n-1)
