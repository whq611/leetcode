class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
