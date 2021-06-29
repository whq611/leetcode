class Solution:
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) != len(s):
            return False
        x = {}
        y = {}
        for i in range(len(s)):
            if pattern[i] in x and x[pattern[i]] != s[i]:
                return False
            if s[i] in y and y[s[i]] != pattern[i]:
                return False
            x[pattern[i]] = s[i]
            y[s[i]] = pattern[i]
        return True
