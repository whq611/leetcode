class Solution:
    def inorderTraversal(self,root):
        res = []
        pre = None
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                tmp = root
                root = root.left
                tem.left = None
            else:
                res.append(root.val)
                root = root.right
        return res
