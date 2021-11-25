class Solution:
    def myPow(self,x,n):
        def help(N):
            if N==0:
                return 1
            y = help(n//2)
            if n%2==0:
                return y*y
            else:
                return y*y*x
        if n>=0:
            return help(n)
        else:
            return 1.0/help(-n)
