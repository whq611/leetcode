class Solution:
    def wordBreak(self,s,wordDict):
        cash = set(wordDict)
        ans = []
        def backtrack(s,tmp,ans):
            if len(s) == 0:
                ans.append(tmp[1:])
                return
            else:
                for i in range(len(s)):
                    if s[:i+1] in cash:
                        backtrack(s[i+1:],tmp+' '+s[:i+1],ans)
        backtrack(s,'',ans)
        return ans
