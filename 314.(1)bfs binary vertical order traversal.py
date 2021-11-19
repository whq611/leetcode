from collections import defaultdict
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self,root):
        columnTable = defaultdict(list)
        queue = [(root,0)]
        while queue:
            node,column = queue.pop(0)
            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left, column-1))
                queue.append((node.right, column+1))
        return [columnTable[x] for x in sorted(columnedTable.keys())]
    
