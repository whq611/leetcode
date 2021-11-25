import collections
class Solution:
    def verticalTraversal(self,root):
        node_list = []
        def dfs(root):
            stack = [(root,0,0)]
            while stack:
                node,row,column = stack.pop(0)
                if node:
                    node_list((column,row,node.val))
                    stack.append((node.left,row+1,column-1))
                    stack.append((node.right,row+1,column+1))
        dfs(root)
        node_list.sorted()
        res = collections.OrderedDict()
        for column,row,value in node_list:
            if column in res:
                res[column].append(value)
            else:
                res[column] = [value]
        return res.values()
