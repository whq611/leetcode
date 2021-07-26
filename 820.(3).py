class Solution:
    def minimumLengthEncoding(self,words):
        n = len(words)
        words.sort(key = lambda word:word[::-1])
        res = 0
        for i in range(n):
            if i+1<n and words[i+1].endswith(words[i]):
                pass
            else:
                res += len(words[i]) + 1
        return res
                                            
            
