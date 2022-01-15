class Solution:
    def maxValue(self, grid):
        m,n = len(grid),len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1,m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for i in range(1,n):
            for j in range(1,m):
                dp[j][i] = grid[j][i] + max(dp[j-1][i],dp[j][i-1])
        return dp[m-1][n-1]
