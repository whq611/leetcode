class Solution:
    def fib(self, n):
        a,b = 0,1
        if n == 0:
            return 0
        if n == 1:
            return 1
        n = n - 2
        while n >= 0:
            c = b
            b = a + b
            a = c
            n -= 1
        return b%1000000007
