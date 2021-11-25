class Solution:
    def myPow(self,x,n):
        def help(N):
            ans = 1.0
            contribute_x = x
            while N>0:
                if N%2 == 1:
                    ans *= contribute_x
                contribute_x *= contribute_x
                N = N//2
            return ans
        if n>=0:
            return help(n)
        else:
            return 1.0/help(-n)
