class Solution:
    def missingNumber(self, nums):
        a = 0
        for i in nums:
            if i != a:
                return a
            a += 1
        return a
