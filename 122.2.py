class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        
        precash = 0
        prehold = -prices[0]
        for i in range(1,len(prices)):
            curcash = max(precash, prehold + prices[i])
            curhold = max(prehold, precash - prices[i])
            precash,prehold = curcash,curhold
        return curcash
