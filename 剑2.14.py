class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        a = [0] * 26
        b = [0] * 26
        for i in range(len(s1)):
            a[ord(s1[i]) - ord('a')] += 1
            b[ord(s2[i]) - ord('a')] += 1
        if a==b: return True
        l,r = 0,len(s1)
        while r<len(s2):
            b[ord(s2[r]) - ord('a')] += 1
            b[ord(s2[l]) - ord('a')] -= 1
            if a==b: return True
            l+=1
            r+=1
        return False
