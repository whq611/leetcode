class Solution:
    def lastRemaining(self, n, m):
        x = 0
        for i in range(2,n+1):
            x = (x+m)%i
        return x
