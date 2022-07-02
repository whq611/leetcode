class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        pre = 0
        a = []
        a.append(0)
        
        for i in range(len(nums)):
            pre += nums[i]
            a.append(pre)
        for i in range(len(nums)):
            if a[i]*2==pre-nums[i]:
                return i

        return -1
