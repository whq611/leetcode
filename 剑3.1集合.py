class Solution:
    def findRepeatNumber(self, nums):
        a = set()
        for i in nums:
            if i in a:
                return i
            a.add(i)
