class Solution:
    def sumNums(self, n):
        return n and (n + self.sumNums(n-1))
