public class l122_2 {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        if (len < 2) {
            return 0;
        }

        // 0：持有现金
        // 1：持有股票
        // 状态转移：0 → 1 → 0 → 1 → 0 → 1 → 0
        

        int precash = 0;
        int prehold = -prices[0];
        int curcash = 0;
        int curhold = -prices[0];
        for (int i = 1; i < len; i++) {
            // 这两行调换顺序也是可以的
            curcash = Math.max(precash, prehold + prices[i]);
            curhold = Math.max(prehold, precash - prices[i]);
            precash = curcash;
            prehold = curhold;
        }
        return curcash;
    }
}
