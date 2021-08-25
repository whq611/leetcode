class Solution:
    def findPeakElement(self, nums):
        # 简单顺序搜索
        nums.append(-float("inf"))
        for i in range(len(nums)):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
