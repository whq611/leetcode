class Solution:
    def longestPalindrome(self, s):
        v = s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if i == 0:
                    if s[j::-1] == s[:j+1] and len(s[:j+1]) > len(v) :
                        v = s[:j+1]
                else:
                    if s[j:i-1:-1] == s[i:j+1] and len(s[i:j+1]) > len(v):
                        v = s[i:j+1]
        return v
