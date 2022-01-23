class Solution:
    def isStraight(self, nums):
        repeat = set()
        ma.mi = 0,14
        for num in nums:
            if num == 0:
                continue
            ma = max(ma,num)
            mi = min(mi,num)
            if num in repeat:
                return False
            repeat.add(num)
        return ma - mi<5
