class Solution:
    def findAnagrams(self, s, p):
        n,m,res = len(s),len(p),[]
        if n < m: return res
        pp = [0] * 26
        ss = [0] * 26

        for i in range(m):
            pp[ord(p[i]) - ord('a')] += 1

        left = 0
        for right in range(n):
            ss[ord(s[right]) - ord('a')] += 1
            while ss[ord(s[right]) - ord('a')] > pp[ord(s[right]) - ord('a')]:
                ss[ord(s[left]) - ord('a')] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        return res
