class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        i=1
        while rowIndex>=i:
            res.append(1)
            for j in range(i-1,0,-1):
                res[j] = res[j] + res[j-1]
            i+=1
        return res
