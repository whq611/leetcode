class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        pre = []
        cur = [1]
        while numRows>1:
            pre = cur
            cur = [1]
            for i in range(len(pre)-1):
                cur.append(pre[i]+pre[i+1])
            cur.append(1)
            res.append(cur)
            numRows-=1
        return res
