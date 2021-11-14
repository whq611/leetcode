class Solution:
    def subsets(self,nums):
        res = [[]]
        for i in range(len(nums)):
            for subres in res[:]:
                res.append(subres+[nums[i]])
        return res
