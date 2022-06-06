class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(a):
            if a==len(s):
                tmp = ''.join(s)
                res.append(tmp[:])
                return
            for i in range(a,len(s)):
                if s[i].isalpha():
                    s[i] = s[i].lower()
                    dfs(i+1)
                    s[i] = s[i].upper()
                if i==len(s)-1:
                    tmp = ''.join(s)
                    res.append(tmp[:])
                    return
            

        res = []
        if not s:
            return res
        s = list(s)


        
        dfs(0)
        return res
