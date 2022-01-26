class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self,root,p,q):
        def getPath(root,target):
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path
        path_p = getPath(root,p)
        path_q = getPath(root,q)
        for u,v in zip(path_p,path_q):
            if u == v:
                ancestor = u
            else:
                break
        return ancestor
