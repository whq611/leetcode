class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = collections.deque([root.left,root.right])
        while(q):
            left = q.popleft()
            right = q.popleft()
            if not left and not right:
                continue
            if (left and not right) or (right and not left):
                return False
            if left.val != right.val:
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True
