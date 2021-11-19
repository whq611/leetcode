from collections import defaultdict
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self,root):
        columnTable = defaultdict(list)
        stack = [(root,0)]
        min_column = max_column = 0

        while stack:
            node,column = stack.pop(0)
            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column,column)
                max_column = max(max_column,column)

                stack.append((node.left, column-1))
                stack.append((node.right, column+1))

        return [columnTable[x] for x in range(min_column,max_column+1)]
