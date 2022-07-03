class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p)>len(s): return res
        a = [0] * 26
        b = [0] * 26
        for i in range(len(p)):
            a[ord(p[i]) - ord('a')] += 1
            b[ord(s[i]) - ord('a')] += 1
        if a==b: res.append(0)
        l,r = 0,len(p)
        while r<len(s):
            b[ord(s[r]) - ord('a')] += 1
            b[ord(s[l]) - ord('a')] -= 1
            
            l+=1
            r+=1
            if a==b: res.append(l)
        return res
