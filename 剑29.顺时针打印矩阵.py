class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        m = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        i,j = 0,0
        

        while True:
            while 0<=i<len(matrix) and 0<=j<len(matrix[0]) and m[i][j] == 0:
                res.append(matrix[i][j])
                m[i][j] = 1
                j += 1
            j -= 1
            i += 1
            if i == len(matrix) or m[i][j] == 1:
                break
            while 0<=i<len(matrix) and 0<=j<len(matrix[0]) and m[i][j] == 0:
                res.append(matrix[i][j])
                m[i][j] = 1
                i += 1
            i -= 1
            j -= 1
            if j<0 or m[i][j] == 1:
                break
            while 0<=i<len(matrix) and 0<=j<len(matrix[0]) and m[i][j] == 0:
                res.append(matrix[i][j])
                m[i][j] = 1
                j -= 1
            j += 1
            i -= 1
            if i<0 or m[i][j] == 1:
                break
            while 0<=i<len(matrix) and 0<=j<len(matrix[0]) and m[i][j] == 0:
                res.append(matrix[i][j])
                m[i][j] = 1
                i -= 1
            i += 1
            j += 1
            if j == len(matrix[0]) or m[i][j] == 1:
                break
        return res
