class Solution:
    def reverseWords(self, s):
        start = end = 0
        a = []
        while end<len(s):
            if s[end] == ' ':
                if start == 0:
                    a.append(s[end-1::-1])
                    start = end + 1
                else:
                    a.append(s[end-1:start-1:-1])
                    start = end + 1
            end += 1
        if start == 0:
            a.append(s[end-1::-1])
        else:
            a.append(s[end-1:start-1:-1])
        return ' '.join(a)
