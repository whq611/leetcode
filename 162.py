class Solution:
    def findPeakElement(self,nums):
        n = len(nums)
        def get(i):
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        l,r = 0,n-1
        while l<=r:
            m = (l+r)//2
            if get(m-1)<get(m)>get(m+1):
                return m
            elif get(m-1)>get(m):
                r = m - 1
            else:
                l = m + 1
