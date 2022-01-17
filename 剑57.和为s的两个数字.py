class Solution:
    def twoSum(self, nums, target):
        a = set()
        for i in nums:
            if target-i in a:
                return [i,target-i]
            else:
                a.add(i)
        return None
