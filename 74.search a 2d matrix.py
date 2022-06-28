class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        i = len(matrix)-1
        j = 0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]==target: return True
            elif matrix[i][j]<target: j+=1
            else: i-=1
        return False
