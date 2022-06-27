# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        a = collections.deque([root])
        b = collections.deque([root.val])
        path = collections.deque([[root.val]])
        while a:
            node = a.popleft()
            cur = b.popleft()
            ans = path.popleft()
            if not node.left and not node.right and cur == targetSum:
                res.append(ans)
            if node.left:
                a.append(node.left)
                b.append(cur+node.left.val)
                ans.append(node.left.val)
                path.append(ans[:])
                ans.pop()
                
            if node.right:
                a.append(node.right)
                b.append(cur+node.right.val)
                ans.append(node.right.val)
                path.append(ans[:])
                ans.pop()
        return res
