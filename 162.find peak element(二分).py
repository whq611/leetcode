class Solution:
    def findPeakElement(self, nums):

        left,right = 0,len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if right - left == 1:
                if nums[right] > nums[left]:
                    return right
                else:
                    return left
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid


            elif nums[mid-1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
