class Solution:
    def removeInvalidParentheses(self, s):
        leftmove,rightmove = 0,0
        for i in s:
            if i == '(':
                leftmove += 1
            elif i == ')':
                if leftmove > 0:
                    leftmove -= 1
                else:
                    rightmove += 1
        res = set()
        def dfs(idx,leftcount,rightcount,leftmove,rightmove,strs):
            if idx == len(s):
                if not leftmove and not rightmove:
                    res.add(strs)
                return
            if s[idx] == '(' and leftmove:
                dfs(idx+1,leftcount,rightcount,leftmove-1,rightmove,strs)
            if s[idx] == ')' and rightmove:
                dfs(idx+1,leftcount,rightcount,leftmove,rightmove-1,strs)
            if s[idx] not in '()':
                dfs(idx+1,leftcount,rightcount,leftmove,rightmove,strs+s[idx])
            elif s[idx] == '(':
                dfs(idx+1,leftcount+1,rightcount,leftmove,rightmove,strs+s[idx])
            elif leftcount > rightcount:
                dfs(idx+1,leftcount,rightcount+1,leftmove,rightmove,strs+s[idx])
            return
        dfs(0, 0, 0, leftmove, rightmove, '')
        return list(res)
