class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i,target):
            l = i+1
            r = n-1
            while l<r:
                if l>i+1 and nums[l]==nums[l-1]:
                    l+=1
                elif nums[l]+nums[r]==target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else: r-=1
                
                
        
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if i==0 or nums[i]!=nums[i-1] and nums[i]<=0:
                twoSum(i,-nums[i])
        return res
