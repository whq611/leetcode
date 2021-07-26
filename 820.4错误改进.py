class Solution:
    def minimumLengthEncoding(self, words):
        words.sort(key = lambda word:word[::-1])
        res2 = ''
        for i in words[::-1]:
            if i + '#' not in res2:
                res2 = res2 + i + '#'
        return len(res2)
