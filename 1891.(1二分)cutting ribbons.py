class Solution:
    def maxLength(self,ribbons,k):
        total = sum(ribbons)
        if k>total:
            return 0
        l,h = 1,total//k
        while l<h:
            m = (l+h+1)//2
            if sum(x//m for x in ribbons) >= k:
                l = m
            else:
                h = m - 1
        return l
