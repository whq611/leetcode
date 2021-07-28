class Solution:
    def findAnagrams(self, s, p):
        n = len(p)
        p = sorted(p)
        res = []
        for i in range(len(s)-n+1):
            if sorted(s[i:i+n]) == p:
                res.append(i)
        return res
