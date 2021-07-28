class Solution:
    def findAnagrams(self, s, p):
        n,m,res = len(s),len(p),[]
        if n < m: return res
        pp = [0] * 26
        ss = [0] * 26
        for i in range(m):
            pp[ord(p[i]) - ord('a')] += 1
            ss[ord(p[i]) - ord('a')] += 1
        if pp == ss:
               res.append(0)

        for i in range(m,n):
               ss[ord(s[i-m]) - ord('a')] -= 1
               ss[ord(s[i]) - ord('a')] += 1
               if ss == pp:
                   res.append(i-m+1)
        return res
