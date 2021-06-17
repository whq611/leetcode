class Solution:
    def twoSum(self,nums,target):
        length = len(nums) 
        for a in range(length):
            for b in range(length):
                if a != b and nums[a] + nums[b] == target:
                    return[a,b]
