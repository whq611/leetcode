import collections
class Solution:
    def customSortString(self,order,s):
        count = collections.Counter(s)
        ans = []
        for c in order:
            ans.append(c*count[c])
            count[c] = 0
        for c in count:
            ans.append(c*count[c])
        return ''.join(ans)
