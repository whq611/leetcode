class Solution:
    def subsets(self,nums):
        res = []
        n = len(nums)

        def helper(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                helper(j+1,tmp+[nums[j]])
        help(0,[])
        return res
