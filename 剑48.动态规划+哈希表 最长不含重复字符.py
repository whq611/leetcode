class Solution:
    def length0fLongestSubstring(self,s):
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j],-1)
            dic[s[j]] = j
            if tmp < j - i:
                tmp += 1
            else:
                tmp = j - i
            res = max(res,tmp)
        return res
