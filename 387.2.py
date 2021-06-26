class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        length = len(s)
        for i in range(length):
            if s.count(s[i]) == 1:
                return i
        return -1
