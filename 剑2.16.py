class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        res = 1
        a = {}
        a[s[0]] = 0
        pre = 1
        for i in range(1,len(s)):
            if s[i] not in a:
                pre = pre+1
                
            else:
                pre = min(pre+1, i-a[s[i]])
            res = max(res,pre)
            a[s[i]] = i
        return res
