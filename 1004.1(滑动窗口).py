class Solution:
    def longestOnes(self, nums, k):

        left = 0
        res = 0
        ans = []
        for right,s in enumerate(nums):
            if s == 0:
                ans.append(right)
            if len(ans) == k + 1:

                left = min(ans) + 1
                ans.remove(left - 1)
            if right - left + 1> res:
                    res = right - left + 1
        return res
