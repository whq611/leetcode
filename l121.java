public class l121 {
    public int maxProfit(int[] prices) {
        int max_profit = 0, min_price = prices[0];
        for(int i:prices){
            if(i>min_price) max_profit = Math.max(max_profit,i-min_price);
            else min_price = i;
        }
        return max_profit;
    }
}
