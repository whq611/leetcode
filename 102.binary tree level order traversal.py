# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = collections.deque([root])
        while queue:
            levels.append([])
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            level += 1
        return levels
