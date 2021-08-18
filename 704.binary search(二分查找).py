class Solution():
    def search(self,nums,target):
        if target not in nums:
            return -1
        left,right = 0,len(nums) - 1
        mid = (left + right) // 2
        while target != nums[mid]:
            if target < nums[mid]:
                right = mid - 1
            if target > nums[mid]:
                left = mid + 1
            mid = (left + right) // 2
        return mid
