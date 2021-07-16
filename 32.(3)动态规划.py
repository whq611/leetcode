class Solution():
    def longestValidParentheses(self,s):
        n = len(s)
        if n == 0 : return 0
        dp = [0] * n
        for i in range(len(s)):
            if s[i] == ')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)
