class Solution:
    def minEatingSpeed(self, piles, h):
        max_count = max(piles)
        if h == len(piles):
            return max_count
        else:
            left = 1
            right = max_count
            while left < right:
                mid = left + (right - left) // 2
                if possible(mid, piles, h):
                    left = mid + 1
                else:
                    right = mid
            return left
def possible(mid,piles,h):
    sum = 0
    for pile in piles:
        if pile % mid == 0:
            sum = sum + int(pile/mid)
        else:
            sum = sum + int(pile / mid) + 1
    return sum > h
