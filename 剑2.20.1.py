class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(2*n-1):
            l = i//2
            r = i//2+i%2
            while(l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
                res+=1
        return res
