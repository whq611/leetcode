class Solution:
    def replaceSpace(self, s):
        a = ''
        for i in s:
            if i == ' ':
                a += '%20'
            else:
                a += i
        return a
