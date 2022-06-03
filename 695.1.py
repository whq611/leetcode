class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(grid,i,j):
            k = 0
            stack = collections.deque([[i,j]])
            while stack:
                i,j = stack.popleft()
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1:
                    grid[i][j] = 0
                    k += 1
                    stack.append([i-1,j])
                    stack.append([i+1,j])
                    stack.append([i,j-1])
                    stack.append([i,j+1])
            return k

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,bfs(grid,i,j))
        return res
