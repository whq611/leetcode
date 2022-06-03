class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            k = 0
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                k += 1
                k += dfs(grid,i-1,j)
                k += dfs(grid,i+1,j)
                k += dfs(grid,i,j-1)
                k += dfs(grid,i,j+1)
                return k
            else: return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,dfs(grid,i,j))
        return res
