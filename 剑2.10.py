class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        a = collections.defaultdict(int)
        res = 0
        pre = 0
        a[0] = 1
        for num in nums:
            pre+=num
            res+=a[pre-k]
            a[pre]+=1
        return res
