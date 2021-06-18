class Solution:
    def twoSum(self,nums,target):
        hashtable = dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[num] = i
        return []
            
