class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        for i in matrix:
            if i[-1] < target:
                continue
            if i[0] > target:
                break
            l = 0
            r = len(matrix[0])-1

            while l<=r:
                m = (l+r)//2
                if i[m] == target:
                    return True
                elif i[m]>target:
                    r -= 1
                else:
                    l += 1
        return False
