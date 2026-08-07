class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l = 0
        maxp = 0
        while(r < len(prices)):
            if(prices[r] > prices[l]):
                profit = prices[r] - prices[l]
                maxp = max(profit, maxp)
            else:
                l=r
            r = r+1
        
        return maxp
