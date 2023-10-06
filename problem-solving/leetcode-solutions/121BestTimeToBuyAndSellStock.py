class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy= 0
        sale= 1
        
        while sale < len(prices):
            
            if prices[sale] > prices [buy]:
                profit = prices[sale] - prices[buy]
                max_profit= max(max_profit, profit)
            else:
                buy = sale
            sale+= 1
                
        return max_profit   
