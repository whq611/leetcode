class Solution:
    def minEatingSpeed(self, piles, h):
        
        l,r = 0,max(piles)
        while l < r:
            res = 0
            m = (l+r)//2
            for i in piles:
                if i <= m:
                    res += 1
                else:
                    while i > m:
                        i = i - m
                        res += 1
                    res += 1
            if res > h:
                l = m + 1
            else:
                r = m
        return l
