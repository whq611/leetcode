class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        a = [0]
        b = 0
        for num in nums:
            b+=num
            a.append(b)
        res = len(nums)+1
        l = r = 0
        while l<=r and r<len(a):
            while r<len(a) and a[r]-a[l]<target:
                r+=1
            res = min(res,r-l)
            l+=1
        if res == len(nums)+1: return 0
        return res
