class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l,r = 0,0
        a = 1
        while l<=r and r<len(nums):
            a*=nums[r]
            while l<=r and a>=k:
                a/=nums[l]
                l+=1
            res += r-l+1

            r+=1
        return res
