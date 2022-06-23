class Solution:
    def longestPalindrome(self, s):
        i,j = 0,len(s)-1
        v = s[0]
        while i < len(s)-1:

            while i<j:
                if i == 0:
                    if s[0] == s[j]:
                        if s[j::-1] == s[:j+1] and len(s[:j+1]) > len(v):
                            v = s[:j+1]
                            break
                    j -= 1
                else:
                    if s[i] == s[j]:
                        if s[j:i-1:-1] == s[i:j+1] and len(s[i:j+1]) > len(v):
                            v = s[i:j+1]
                            break
                    j -= 1
            i += 1
            j = len(s)-1
        return v
