class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        res = [0] * (len(nums)-1)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)-1):
            res[i] = max(res[i-2] + nums[i], res[i-1])
        a = res[-1]
        res = [0] * len(nums)
        res[0] = 0
        res[1] = nums[1]
        for i in range(2,len(nums)):
            res[i] = max(res[i-2] + nums[i], res[i-1])
        b = res[-1]
        return max(a,b)
