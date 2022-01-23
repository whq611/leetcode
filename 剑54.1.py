class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def kthLargest(self, root, k):
        def dfs(root):
            if not root or self.k == 1:
                return
            dfs(root.left)
            self.k -= 1
            if self.k == 1:
                self.res = root.val
            dfs(root.right)

            self.k = k
            dfs(root)
            return self.res
