# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return [] 
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    def rangeSumBST(self, root, low, high):
        self.root = root
        a = self.inorderTraversal(self.root)
        sum = 0
        for i in a:
            if i>=low and i<=high:
                sum += i
        return sum
    
