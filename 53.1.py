class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        total = 0
        for i in range(len(nums)):
            if total>0:
                total += nums[i]
            else:
                total = nums[i]
            res = max(res,total)
        return res
