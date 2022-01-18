class Solution:
    def reverseWords(self, s):
        s = s.split()
        return ' '.join(s[::-1])
