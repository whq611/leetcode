class Solution:
    def findAnagrams(self, s, p):
        n,m,res = len(s),len(p),[]
        if n<m: return res
        pp,a = [0] * 26,[0] * 26

        for i in range(m):
            pp[ord(p[i]) - ord('a')] += 1
            pp[ord(s[i]) - ord('a')] -= 1
        if pp == a:
            res.append(0)

        for i in range(m,n):
            pp[ord(s[i - m]) - ord('a')] += 1
            pp[ord(s[i]) - ord('a')] -= 1
            if pp == a:
                res.append(i-m+1)
        return res
