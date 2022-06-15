class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]
        pre = []
        while(rowIndex>=1):
            cur = [1]
            for i in range(len(pre)-1):
                cur.append(pre[i]+pre[i+1])
            cur.append(1)
            pre.clear()
            pre = cur
            rowIndex-=1
        return cur
