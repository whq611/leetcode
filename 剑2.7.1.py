class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        seen = set()
        for i in range(n):
            if nums[i] not in seen:
                dup = set()
                for j in range(i+1,n):
                    if -nums[i]-nums[j] in dup:
                        res.add(tuple(sorted((nums[i],nums[j],-nums[i]-nums[j]))))
                    dup.add(nums[j])
                
        
        
        return list(res)
