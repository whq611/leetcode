class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n<m: return ""
        cnt = [0] * 150
        k=0
        for c in t:
            cnt[ord(c) - ord('A')]+=1
            if cnt[ord(c) - ord('A')]==1: k+=1
        l = r = 0
        i = 0
        
        for j in range(n):
            cnt[ord(s[j]) - ord('A')] -= 1
            if cnt[ord(s[j]) - ord('A')]==0: k-=1
            if k==0:

                while cnt[ord(s[i]) - ord('A')]<0:
                    cnt[ord(s[i]) - ord('A')] += 1
                    i+=1
                if l==r or j-i+1<r-l:
                    r = j+1
                    l = i
        
        return s[l:r]
