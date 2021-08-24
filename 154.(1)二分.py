class Solution:
    def findMin(self, nums):
        low,high = 0,len(nums) - 1
        while low < high:
            m = low + (high - low) // 2
            if nums[m] < nums[high]:
                high = m
            elif nums[m] > nums[high]:
                low = m + 1
            else:
                high -= 1
        return nums[low]
