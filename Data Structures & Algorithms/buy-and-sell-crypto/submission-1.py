class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high =1
        max_profit=0
        while (high < len(prices)):
            if prices[high]<prices[low]:
                low=high
            
            else:
                profit=prices[high]-prices[low]
                max_profit=max(max_profit,profit)
            
            high+=1
        return max_profit