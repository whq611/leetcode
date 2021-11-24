class Solution:
    def depthSum(self,nestedList):
        def dfs(nestedList,depth):
            total = 0
            for nested in nestedList:
                if nested.isInteger():
                    total += nested.getInteger()*depth
                else:
                    total += dfs(nested.getList(),depth+1)
            return total
        return dfs(nestedList,1)
