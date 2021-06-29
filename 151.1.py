class Solution:
    def reverseWords(self, s):
        s = s.split()
        s = s[::-1]
        return ' '.join(s)
