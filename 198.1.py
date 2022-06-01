class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        slow = nums[0]
        fast = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            tmp = max(slow + nums[i], fast)
            slow = fast
            fast = tmp
        return fast
