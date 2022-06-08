class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        summ = [0] * (n+1)
        for i in range(1,n+1):
            summ[i] = summ[i-1] + nums[i-1]
        MOD = 1000000007
        ans = 0
        l,r = 2,2
        for i in range(1,n-1):
            l = max(l,i+1)
            r = max(r,i+1)
            while r<n and summ[n]-summ[r]>=summ[r]-summ[i]:
                r+=1
            while l<n and summ[l] - summ[i] < summ[i]:
                l+=1
            if r>=l:
                ans += r-l
        return ans%MOD
