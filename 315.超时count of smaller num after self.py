import bisect
class Solution:
    def countSmaller(self, nums):
        
        l = len(nums)
        counts = [0] * l
        a = 0
        while a < l - 1:
            counts[a] = bisect.bisect_left(sorted(nums[a+1:]),nums[a])
            a += 1
        return counts
