class Solution:
    def minimumLengthEncoding(self,words):
        words = list(set(words))
        trie = {}
        nodes = []
        for word in words:
            now = trie
            for w in reversed(word):
                if w in now:
                    now = now[w]
                else:
                    now[w] = {}
                    now = now[w]
            nodes.append(now)
        ans = 0
        for w,c in zip(words,nodes):
            if len(c) == 0:
                ans += len(w) + 1
        return ans
