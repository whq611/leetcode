class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        l = r = summ = 0
        while l<=r and r<len(nums):
            summ+=nums[r]
            while l<=r and summ>=target:
                res = min(res,r-l+1)
                summ-=nums[l]
                l+=1
            r+=1
        if res==len(nums)+1: return 0
        return res
