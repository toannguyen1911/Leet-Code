class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) == 1):
            return 0;
        
        max_profit = 0;
        buy_d = 0;
        sell_d = 1;
        
        while sell_d < len(prices):
            current_profit = prices[sell_d] - prices[buy_d];
            if prices[buy_d] < prices[sell_d]:
                max_profit = max(current_profit, max_profit);
            else:
                buy_d = sell_d
            sell_d += 1
    
        return max_profit;
            
            
        