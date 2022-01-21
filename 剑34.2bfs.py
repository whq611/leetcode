class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
class Solution:
    def pathSum(self,root,target):
        ret = list()
        parent = collections.defaultdict(lambda:None)
        def getPath(node):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = parent[node]
            ret.append(tmp[::-1])
        if not root:
            return ret
        que_node = collections.deque([root])
        que_total = collections.deque([0])
        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val
            if not node.left and not node.right:
                if rec == target:
                    getPath(node)
                else:
                    if node.left:
                        parent[node.left] = node
                        que_node.append(node.left)
                        que_total.append(rec)
                    if node.right:
                        parent[node.right] = node
                        que_node.append(node.right)
                        que_total.append(rec)
        return ret
                
