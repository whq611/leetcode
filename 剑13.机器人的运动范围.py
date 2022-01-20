class Solution:
    def movingCount(self, m, n, k):
        def dfs(i,j):
            if (i,j) not in dic and 0<=i<m and 0<=j<n and i%10+i//10+j%10+j//10 <=k :
                self.res += 1
                dic[(i,j)] = 1
                dfs(i,j-1)
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j+1)
                
            else:
                return 
        self.res = 0
        dic = {}
        dfs(0,0)
        return self.res
