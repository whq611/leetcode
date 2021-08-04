import collections
class Solution:
    def minWindow(self, s, t):
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needcnt = len(t)
        i = 0
        res = (0,float('inf'))
        for j,c in enumerate(s):
            if need[c] > 0:
                needcnt -= 1
            need[c] -= 1
            if needcnt == 0:
                while True:
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i,j)
                need[s[i]] += 1
                needcnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
                
            
        
