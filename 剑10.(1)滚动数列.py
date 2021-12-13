class Solution:
    def fib(self,n):
        if n<2:
            return n
        MOD = 10 ** 9 + 7
        p,q,r = 0,0,1
        for i in range(2,n+1):
            p = q
            q = r
            r = (p+q)%MOD
        return r
