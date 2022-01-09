class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        res = []
        tmp = [root]
        while tmp:
            tem = []
            for i in range(len(tmp)):
                node = tmp.pop(0)
                tem.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(tem)
        return res
