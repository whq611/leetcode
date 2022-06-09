public class lj63 {
    public int maxProfit(int[] prices) {
        if(prices.length<2) return 0;
        int res = 0, buy = prices[0];
        for(int i=1; i<prices.length; i++){
            if(prices[i]<buy) buy = prices[i];
            else res = Math.max(res, prices[i]-buy);
        }
        return res;
    }
}
