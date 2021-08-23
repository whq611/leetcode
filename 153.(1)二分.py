class Solution:
    def findMin(self, nums):
        low,high = 0,len(nums) - 1
        while low < high:
            m = low + (high - low) // 2
            if nums[m] < nums[high]:
                high = m
            else:
                low = m + 1
        return nums[low]
