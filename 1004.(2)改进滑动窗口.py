class Solution:
    def longestOnes(self, nums, k):
        N = len(nums)
        res = 0
        left, right = 0, 0
        zeros = 0 
        while right < N:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
