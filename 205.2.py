class Solution:
    def isIsomorphic(self, s, t):
        x = {}
        y = {}
        for i in range(len(s)):
            if s[i] in x and x[s[i]] != t[i]:
                return False
            if t[i] in y and y[t[i]] != s[i]:
                return False
            x[s[i]] = t[i]
            y[t[i]] = s[i]
        return True
