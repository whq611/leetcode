class Solution:
    def longestSubstring(self,s,k):
        n = len(s)
        for c in range(n)[::-1]:
            a = 0
            while a + c < n:
                less = 0
                cnt = {chr(i+97):0 for i in range(26)}
                for b in s[a:a+c+1]:
                    cnt[b] += 1
                    if cnt[b] == 1:
                        less += 1
                    if cnt[b] == k:
                        less -= 1
                if less == 0:
                    return c + 1
                a += 1
        return 0
