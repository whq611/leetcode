# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        dic = {}
        stack = [cur]
        while stack:
            cur = stack.pop()
            if cur.left:
                dic[cur.left] = cur
                stack.append(cur.left)
            if cur.right:
                dic[cur.right] = cur
                stack.append(cur.right)
        a = set()
        
        while p in dic:
            a.add(p)
            p = dic[p]
        a.add(p)
        while q not in a:
            q = dic[q]
        return q
