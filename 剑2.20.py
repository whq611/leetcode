class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if(s[i]==s[j] and (j-i<=1 or dp[i+1][j-1])):
                    dp[i][j] = True
                    res+=1
        return res
