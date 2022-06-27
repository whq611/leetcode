class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        tmp = ''
        res=''
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            if s[i]==')':
                if l==0: continue
                l-=1
            tmp+=s[i]

        for j in range(len(tmp)-1,-1,-1):
            if tmp[j]==')':
                r+=1
            if tmp[j]=='(':
                if r==0: continue
                r-=1
            res = tmp[j] + res
        return res
