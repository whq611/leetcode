class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        diff = 0
        if n>m:
            return False
        cnt1 = [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - ord('a')] -= 1
            cnt1[ord(s2[i]) - ord('a')] += 1
        for i in cnt1:
            if i!=0:
                diff += 1
        if diff==0:
            return True
        for i in range(n,m):
            x = ord(s2[i]) - ord('a')
            y = ord(s2[i-n]) - ord('a')
            if x==y: continue
            if cnt1[x]==0: diff+=1
            cnt1[x]+=1
            if cnt1[x]==0: diff-=1
            if cnt1[y]==0: diff+=1
            cnt1[y]-=1
            if cnt1[y]==0: diff-=1
            if diff==0: return True

        return False
