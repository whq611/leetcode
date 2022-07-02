class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        a = {}
        b = 0
        res = 0
        a[0] = -1
        for i in range(len(nums)):
            if nums[i]==1:
                b += 1
            else:
                b -= 1
            if b in a:
                res = max(res,i-a[b])
            else:
                a[b] = i



        return res
