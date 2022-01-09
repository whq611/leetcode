class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        tmp = [root]
        a = 0
        while tmp:
            tem = []
            for i in range(len(tmp)):
                node = tmp.pop(0)
                if a == 0:
                    tem.append(node.val)
                else:
                    tem.insert(0,node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if a == 0:
                a = 1
            else:
                a = 0
            res.append(tem)
        return res
