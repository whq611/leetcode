class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            a = s[:i] + s[i+1:]
            if a==a[::-1]: return True
        return False
