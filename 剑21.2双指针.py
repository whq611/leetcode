class Solution:
    def exchange(self,nums):
        i,j = 0,len(nums)-1
        while i<j:
            while i<j and nums[i]&1 == 1:
                i += 1
            while i<j and nums[j]&1 == 1:
                j -= 1
        return nums
