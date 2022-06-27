# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        cur = collections.deque([root])

        a = []
        while cur:
            for i in range(len(cur)):
                node = cur.popleft()
                a.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(a[-1])

        return res
