class Solution:
    def generateParentthesis(self,n):
        res = []
        cur = ''
        def dfs(cur,left,right,n):
            if left == n and right == n:
                res.append(cur)
            if left<right:
                return
            if left<n:
                dfs(cur+'(',left+1,right,n)
            if right<n:
                dfs(cur+')',left,right+1,n)
        dfs(cur,0,0,n)
        return res
