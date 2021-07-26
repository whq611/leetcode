class Solution:
    def minimumLengthEncoding(self,words):
        res1 = res2 = ''
        for i in words:
            if i + '#' not in res1:
                res1 = res1 + i + '#'
        for i in words[::-1]:
            if i + '#' not in res2:
                res2 = res2 + i + '#'
        return min(len(res1),len(res2))
