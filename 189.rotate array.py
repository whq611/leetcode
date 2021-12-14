class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[-k%n:] + nums[:-k%n]
        
