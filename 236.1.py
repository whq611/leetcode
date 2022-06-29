# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur):
            if cur.left:
                dic[cur.left] = cur
                dfs(cur.left)
            if cur.right:
                dic[cur.right] = cur
                dfs(cur.right)
        
        cur = root
        dic = {}
        dfs(cur)
        p1 = p
        q1 = q
        while p1!=q1:
            if p1 in dic:
                p1 = dic[p1]
            else: p1 = q
            if q1 in dic: q1 = dic[q1]
            else: q1 = p
        return q1
