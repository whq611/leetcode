class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = collections.deque([])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if  grid[i][j] == 1:
                    count+=1
        if count==0:
            return 0
        minute = 0
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                for d in dir:
                    x = node[0]+d[0]
                    y = node[1]+d[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append([x,y])
            minute += 1
        for row in grid:
            for i in row:
                if i == 1:#还有新鲜的
                    return -1
        return minute-1
