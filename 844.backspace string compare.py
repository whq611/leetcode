class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        a = 0
        while i>=0 or j>=0:
            while (i>=0 and s[i]=='#') or a:
                if i>=0 and s[i]=='#':
                    i-=1
                    a+=1
                else:
                    i-=1
                    a-=1
            while (j>=0 and t[j]=='#') or a:
                if j>=0 and t[j]=='#':
                    j-=1
                    a+=1
                else:
                    j-=1
                    a-=1
            if i>=0 and j>=0: 
                if s[i]==t[j]:
                    i-=1
                    j-=1
                else: return False
            elif i>=0 or j>=0: return False
        return i<0 and j<0
