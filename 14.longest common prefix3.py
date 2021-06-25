class Solution:
    def longestCommonPrefix(self,strs):
        def lcp(start,end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            lcpleft,lcpright = lcp(start,mid),lcp(mid+1,end)
            minlength = min(len(lcpleft),len(lcpright))
            for i in range(minlength):
                if lcpleft[i] != lcpright[i]:
                    return lcpleft[:i]
            return lcpleft[:minlength]
        return '' if not strs else lcp(0,len(strs)-1)
    
