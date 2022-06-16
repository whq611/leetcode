class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        l,r,t,b = 0,n-1,0,n-1
        m = 1
        while True:
            for i in range(l,r+1):
                res[t][i] = m
                m+=1
            t+=1
            for i in range(t,b+1):
                res[i][r] = m
                m+=1
            r-=1
            for i in range(r,l-1,-1):
                res[b][i] = m
                m+=1
            b-=1
            for i in range(b,t-1,-1):
                res[i][l] = m
                m+=1
            l+=1
            if l>r or t>b: break
        return res
