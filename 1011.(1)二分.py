class Solution:
    def shipWithinDays(self,weights,D):
        lo, hi = max(weights), sum(weights)
        while(lo < hi):
            mid = (lo + hi) // 2
            temp = 0
            day = 1
            for weight in weights:
                temp += weight
                if temp > mid:
                    day += 1
                    temp = weight

            if day > D:
                lo = mid + 1
            elif day <= D:
                hi = mid
        return lo
