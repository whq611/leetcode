class Solution:
    def permutation(self, s):
        self.res = []
        n = len(s)

        def backtrack(s,path):
            if not s:
                self.res.append(path)
            seen = set()
            for i in range(len(s)):
                if s[i] in seen:
                    continue
                seen.add(s[i])
                backtrack(s[:i]+s[i+1:], path+s[i])

        backtrack(s,"")
        return self.res
