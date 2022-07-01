class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        product = 1
        n = len(nums)
        if n==0: return 0
        l = r = 0 
        while l<=r and r<n:
            product *= nums[r]
            while l<=r and product>=k:
                product //= nums[l]
                l+=1
            res += r-l+1
            r+=1
        
        return res
