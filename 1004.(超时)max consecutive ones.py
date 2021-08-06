class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        for i in range(n+1)[::-1]:
            j = 0 
            while j+i<n+1:
                if nums[j:j+i].count(0)<= k:
                    return i
                j += 1
