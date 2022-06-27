# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        a = 0
        cur = collections.deque([root])
        res = [[root.val]]
        
        while True:
            
            x = []
            nex = []
            while cur:
                node = cur.popleft()
                if node.left:
                    nex.append(node.left)
                    x.append(node.left.val)
                if node.right:
                    nex.append(node.right)
                    x.append(node.right.val)
            if not x: break
            if a%2==0:
                res.append(x[::-1])
            else:
                res.append(x)
            cur = collections.deque(nex)
            a+=1
        return res
