# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root.left and not root.right: return False
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        a = inorder(root)
        i,j = 0, len(a)-1
        while(i<j):
            if a[i]+a[j]==k:
                return True
            elif a[i]+a[j]<k:
                i+=1
            else:
                j-=1
        return False
