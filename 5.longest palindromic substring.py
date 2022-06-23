class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            for j in range(i+1):
                if i-j+1<=len(res):
                    break
                if s[j:i+1] == s[j:i+1][::-1] and i-j+1>len(res):
                    res = s[j:i+1]
                    break
        return res
