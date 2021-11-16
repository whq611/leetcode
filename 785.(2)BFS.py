class Solution:
    def isBipartite(self,graph):
        n = len(graph)
        uncolored,red,green = 0,1,2
        color = [uncolored]*n
        for i in range(n):
            if color[i] == uncolored:
                q = [i]
                color[i] = red
                while q:
                    node = q.pop()
                    if color[node] == red:
                        a = green
                    else:
                        a = red
                    for neighbor in graph[node]:
                        if color[neighbor] == uncolored:
                            q.append(neighbor)
                            color[neighbor] = a
                        elif color[neighbor] != a:
                            return False
        return True
