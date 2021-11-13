class Solution:
    def rotate(self,matrix):
        n = len(maxtrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_new
        return matrix
