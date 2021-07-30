class Solution:
    def lengthOfLongestSubstring(self, s):
        occ = set()
        n = len(s)
        rk,ans = -1,0
        for i in range(n):
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            occ.remove(s[i])
            ans = max(ans,rk - i + 1)
        return ans
