class Solution:
    def myPow(self, x, n):
        if n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        elif n>1:
            if n%2==0:
                return self.myPow(x*x,n//2)
            else:
                return self.myPow(x*x,n//2)*x
        elif n==1:
            return x
            
