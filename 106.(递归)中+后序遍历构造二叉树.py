class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def buildTree(self,inorder,postorder):
        def myBuildTree(postorder_left,postorder_right,inorder_left,inorder_right):
            if postorder_left>postorder_right:
                return None
            postorder_root = postorder_right
            inorder_root = index[postorder[postorder_right]]
            root = TreeNode(postorder[postorder_right])
            size_left_subtree = inorder_root - inorder_left
            root.left = myBuildTree(postorder_left,postorder_left+size_left_subtree-1,inorder_left,inorder_root-1)
            root.right = myBuildTree(postorder_left+size_left_subtree,postorder_right-1,inorder_root+1,inorder_right)
            return root            


        n = len(postorder)
        index = {element:i for i,element in enumerate(inorder)}
        return myBuildTree(0,n-1,n,n-1)
