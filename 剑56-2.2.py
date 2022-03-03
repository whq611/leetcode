class Solution:
    def singleNumber(self, nums):
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                count[j] += num&1
                num >>= 1
        res = 0
        m = 3
        for i in range(32):
            res <<= 1
            res |= counts[31-i]%m
        return res if counts[31]%m == 0 else ~(res^0xffffffff)
