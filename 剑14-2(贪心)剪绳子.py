class Solution:
    def cuttingRope(self, n):
        if n<=3:
            return n-1
        a,b,p = n//3,n%3,1000000007
        if b==0:
            return 3**a%p
        elif b == 1:
            return 3**(a-1)*4%1000000007
        else:
            return 3**a*2%p
