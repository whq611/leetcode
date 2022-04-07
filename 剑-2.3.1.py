class Solution:
    def countBits(self, n):
        def count(x):
            ones = 0
            while x>0:
                x &= (x-1)
                ones += 1
            return ones
        bits = [count(i) for i in range(n+1)]
        return bits
