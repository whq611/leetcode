# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root,targetSum,cur):
            
            targetSum -= root.val
            cur.append(root.val)
            if not root.left and not root.right and targetSum == 0:
                res.append(cur[:])
            if root.left:
                dfs(root.left, targetSum, cur)
                cur.pop()
            if root.right:
                dfs(root.right, targetSum, cur)
                cur.pop()
        
        if not root:
            return []
        res = []
        cur = []
        dfs(root,targetSum,cur)
        return res
