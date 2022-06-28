class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        l,r = 0,len(nums)-1
        while l<=r:
            m = l+(r-l)//2
            if nums[m]>=target:
                r = m-1
            else:
                l = m+1
        i = r

        l,r = 0,len(nums)-1
        while l<=r:
            m = l+(r-l)//2
            if nums[m]>target:
                r = m-1
            else:
                l = m+1
        j = l
        if j-i<=1: return [-1,-1]
        return [i+1,j-1]
