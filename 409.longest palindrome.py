class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = {}
        res = 0
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]] += 1
            else:
                a[s[i]] = 1
        b = False
        for i in a:
            if a[i]%2==0: res+=a[i]
            else:
                b = True 
                res+=a[i]-1
        if b: return res+1
        else: return res
