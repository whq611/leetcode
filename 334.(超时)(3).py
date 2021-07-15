class Solution:
    def increasingTriplet(self,nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
                    if dp[i] == 3:
                        return True
        return False
                
