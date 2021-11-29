class Solution:
    def findDiagonalOrder(self,mat):
        if not matrix or not matrix[0]:
            return []
        m,n = len(mat),len(mat[0])
        row,col = 0,0
        res = []
        direction = 1
        while row<m and col<n:
            res.append(mat[row][col])
            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)
            if new_row<0 or new_row==m or new_col<0 or new_col==n:
                if direction:
                    row += (col == n-1)
                    col += (col < n-1)
                else:
                    col += (row == m-1)
                    row += (row < m-1)
                direction = 1 - direction
            else:
                row = new_row
                col = new_col
        return res
            
