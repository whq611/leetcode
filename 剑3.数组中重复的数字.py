class Solution:
    def findRepeatNumber(self, nums):
        a = len(nums)
        for i in range(a):
            if nums.index(nums[i]) != i:
                return nums[i]
