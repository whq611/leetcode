class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(mat,i,j):
            ans = 0
            stack = collections.deque([])
            stack.append([i,j])

            while stack:
                l = len(stack)
                for _ in range(l):
                    a,b = stack.popleft()
                    if 0<=a<len(mat) and 0<=b<len(mat[0]) and mat[a][b] == 0:
                        res[i][j] = ans
                        return
                    if 0<=a<len(mat) and 0<=b<len(mat[0]) and mat[a][b] != 0:
                        stack.append([a-1,b])
                        stack.append([a+1,b])
                        stack.append([a,b-1])
                        stack.append([a,b+1])
                ans += 1




        res = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    bfs(mat,i,j)
        return res
