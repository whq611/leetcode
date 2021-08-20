class Solution:
    def search(self, nums, target):
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                 if nums[mid] < target <= nums[right]:
                    left = mid + 1
                 else:
                    right = mid - 1           
        return -1
