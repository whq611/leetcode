class Solution:
    def isBipartite(self,graph):
        n = len(graph)
        uncolored,red,green = 0,1,2
        color = [uncolored]*n
        valid = True

        def dfs(node,c):
            nonlocal valid
            color[node] = c
            if c == red:
                a = green
            else:
                a = red
            for neighbor in graph[node]:
                if color[neighbor] == uncolored:
                    dfs(neighbor,a)
                    if not valid:
                        return
                elif color[neighbor] != a:
                    valid = False
                    return

        for i in range(n):
            if color[i] == uncolored:
                dfs(i,red)
                if not valid:
                    break
        return valid
