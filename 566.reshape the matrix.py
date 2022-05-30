class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        res = [[0]*c for _ in range(r)]
        a,b =0,0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[a][b] = mat[i][j]
                if b + 1 == c:
                    b = 0
                    a += 1
                else:
                    b += 1
        return res
