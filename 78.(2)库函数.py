from itertools import combinations
class Solution:
    def subsets(self, nums):
        res = []
        for i in range(len(nums)+1):
            for tmp in list(combinations(nums, i)):
                res.append(tmp)
        return res
