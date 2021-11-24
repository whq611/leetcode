class Solution:
    def ShortestDistance(self,grid):
        def bfs(i,j):
            visited = {(i,j)}
            buildings = set()
            q = [(i,j,0)]
            total_step = 0
            dirs = [[0,1],[0,-1],[-1,0],[1,0]]

            while q:
                i,j,step = q.pop(0)
                if grid[i][j] == 1 and (i,j) not in buildings:
                    total_step += step
                    buildings.add((i,j))
                if len(buildings) == num_buidings:
                    return total_step
                if grid[i][j] == 0:
                    for d in dirs:
                        x = i + d[0]
                        y = j + d[1]
                        if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y]!=2:
                            return -1
        m,n = len(grid),len(grid[0])
        num_buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_buildings += 1
        min_step = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_step = dfs(i,j)
                    if total_step != -1 and min_step>total_step:
                        min_step = total_step
        return min_step if min_step != float('inf') else -1
            
            
