class Solution:
    def isToeplitzMatrix(self,matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        if row_len == 0 or col_len == 0:
            return True
        for i in range(row_len-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True
