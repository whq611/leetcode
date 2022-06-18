class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        a = [nums[0]]
        for i in range(1,len(nums)):
            a.append(a[-1]+nums[i])
        b = {}
        count = 0
        for i in a:
            if i==k:
                count+=1
            if i-k in b:
                count+=b[i-k]
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        return count
        
