import collections
class Solution:
    def minWindow(self, s, t):
        if not t or not s or len(s) < len(t):
            return ''
        m = collections.defaultdict(int)
        n = collections.defaultdict(int)
        for c in t:
            m[c] += 1
        left = 0
        right = 0
        distance = 0
        minlen = len(s) + 1
        while right < len(s):
            if n[s[right]] < m[s[right]]:
                distance += 1
            n[s[right]] += 1
            right += 1
            while distance == len(t):
                if n[s[left]] > m[s[left]]:
                    n[s[left]] -= 1
                    left += 1
                else:
                    if right - left < minlen:
                        minlen = right - left
                        sub = [left,right]
                    n[s[left]] -= 1
                    left += 1
                    distance -= 1
        if minlen == len(s) + 1:
            return ''
        else:
            return s[sub[0]:sub[1]]
                        
        
