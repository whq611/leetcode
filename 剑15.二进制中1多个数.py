class Solution:
    def hammingWeight(self, n):
        res = 0
        while n!=0:
            i = n%2
            if i == 1:
                res += 1
            n //= 2
        return res
