class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):return False
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        for i in counts:
            if i != 0:
                return False
        return True
