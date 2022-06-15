class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex+1)
        i=2
        while rowIndex>=i:
            for j in range(i-1,0,-1):
                res[j] = res[j] + res[j-1]
            i+=1
        return res
