class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setA = set()
        setB = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    setA.add(i)
                    setB.add(j)
        for i in setA:
            matrix[i] = [0] * len(matrix[0])
        for j in setB:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        return matrix
