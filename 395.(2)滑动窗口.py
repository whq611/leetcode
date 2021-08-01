class Solution:
    def longestSubstring(self,s,k):
        ans = 0
        for i in range(1,27):
            left = right = 0
            tn = 0
            less = 0
            cnt = {chr(i+97):0 for i in range(26)}
            while right <= len(s) - 1:
                cnt[s[right]] += 1
                if cnt[s[right]] == 1:
                    tn += 1
                    less += 1
                if cnt[s[right]] == k:
                    less -= 1
                while tn > i:
                    cnt[s[left]] -= 1
                    if cnt[s[left]] == 0:
                        tn -= 1
                        less -= 1
                    if cnt[s[left]] == k - 1:
                        less += 1
                    left += 1
                if tn == i and less == 0:
                    ans = max(right - left + 1,ans)
                right += 1
        return ans
                    
