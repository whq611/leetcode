# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.a = {}        
        def bfs(cur):
    
            if cur.left:
                self.a[cur.left] = cur
                bfs(cur.left)
            if cur.right:
                self.a[cur.right] = cur
                bfs(cur.right)
        bfs(root)
        b = set()
        cur = p
        while p:
            b.add(p)
            if self.a.get(p):
                p = self.a[p]
            else:
                break
        while q:
            if q in b:
                return q
            if self.a.get(q):
                q = self.a[q]
            else:
                return None
