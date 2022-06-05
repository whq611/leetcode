class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def dfs(i,j,level):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and (grid[i][j]==1 or grid[i][j]>=level):
                grid[i][j] = level
                level += 1
                dfs(i - 1, j, level)
                dfs(i + 1, j, level)
                dfs(i, j - 1, level)
                dfs(i, j + 1, level)

        if not grid or len(grid)==0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    dfs(i,j,2)
        maxLevel = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
                    
                maxLevel = max(maxLevel, grid[i][j])
        if maxLevel==0: return 0
        return maxLevel-2
