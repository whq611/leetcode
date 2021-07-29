class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        n = len(s)
        res = []
        for i in range(n):
            j = n
            while j>i:
                if len(s[i:j]) == len(set(s[i:j])):                   
                    res.append(s[i:j])
                    break
                else:
                    j -= 1
        return max(len(i)for i in res)
