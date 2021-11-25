class Solution:
    def removeInvalidParentheses(self,s):
        l=r=0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = []
        @lru_cache(None)
        def dfs(idx,cl,cr,dl,dr,path):
            if idx == len(s):
                if not dl and not dr:
                    ans.append(path)
                return
            if cr>cl or dl>0 or dr>0:
                return
            c = s[idx]
            if c == '(':
                dfs(idx+1,cl,cr,dl-1,dr,path)
                dfs(idx+1,cl+1,cr,dl,dr,path+c)
            elif c == ')':
                dfs(idx+1,cl,cr,dl,dr-1,path)
                dfs(idx+1,cl,cr+1,dl,dr,path+c)
            else:
                dfs(idx+1,cl,cr,dl,dr,path+c)
        dfs(0,0,0,l,r,'')
        return ans

