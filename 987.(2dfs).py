import collections
class Solution:
    def verticalTraversal(self,root):
        node_list = []
        def dfs(node,row,column):
            if node:
                node_list.append((column,row,node.val))
                dfs(node.left,row+1,column-1)
                dfs(node.right,row+1,column+1)
        dfs(root,0,0)
        node_list.sort()
        res = collection.OrderedDict()
        for column,row,value in node_list:
            if column in res:
                res[column].append(value)
            else:
                column[column] = [value]
        return res.values()
