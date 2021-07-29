class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        a = n = len(s)
        while a > 0:
            for i in range(n-a+1):
                if len(s[i:i+a]) == len(set(s[i:i+a])):
                    return a
            a -= 1
        
