class Solution:
    def exchange(self, nums):
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                a = nums[i]
                nums.pop(i)
                nums.insert(0,a)
        return nums
