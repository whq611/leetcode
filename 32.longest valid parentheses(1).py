class Solution:
    def longestValidParentheses(self,s):
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if stack and s[i] == ')':
                res.append(stack.pop())
                res.append(i)
        res.sort()
        i = 0
        ans = 0
        n = len(res)
        while i<n:
            j = i
            while j<n-1 and res[j+1] == res[j] + 1:
                j += 1
            ans = max(ans,j-i+1)
            i = j + 1
        return ans
            
