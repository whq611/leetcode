class Solution:
    def firstUniqChar(self, s):
        if s == "":
            return " "
        for i in range(0, len(s)):
            if s.count(s[i]) == 1:
                return s[i]
        return " "
