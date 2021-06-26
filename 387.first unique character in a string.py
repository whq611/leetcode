class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        length = len(s)
        for i in range(length):
            for j in range(length):
                if s[i] == s[j] and j != i:
                    break
                if j == length - 1:
                    return i
        return -1
