# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find(node):
            if not node:
                return False
            if k-node.val in a:
                return True
            a.add(node.val)
            return find(node.left) or find(node.right)
        a = set()
        return find(root)
