class Solution:
    def searchRange(self,nums,target):
        if not nums:
            return [-1,-1]
        res = list()
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            return[-1,-1]
        res.append(l)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        res.append(r)
        return res

        
