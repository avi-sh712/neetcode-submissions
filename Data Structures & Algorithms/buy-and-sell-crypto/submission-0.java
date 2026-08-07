class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int profit = 0;

        while(r < prices.length){
            if(prices[r] > prices[l]){
                int p = prices[r] - prices[l];
                profit = Math.max(profit, p);
            }else{
                l=r;
            }
            r++;
        }
        return profit;

    }
}
