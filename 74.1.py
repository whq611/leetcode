class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        l = 0
        r = len(matrix)-1
        while l<=r:
            m = l + (r-l)//2
            if matrix[m][0]>target: r = m-1
            else: l = m+1
        i = r
        if i<0: return False
        l = 0
        r = len(matrix[0])-1
        while l<=r:
            m = l + (r-l)//2
            if matrix[i][m]==target: return True
            elif matrix[i][m]>target: r = m-1
            else: l = m+1
        return False

