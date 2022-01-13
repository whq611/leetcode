class Solution:
    def maxProfit(self,prices):
        if len(prices)<2:
            return 0
        buy = prices[0]
        res = 0
        for i in prices[1:]:
            if i < buy:
                buy = i
            else:
                res = max(res,i - buy)
        return res
