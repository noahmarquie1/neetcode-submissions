class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        buy = 0
        sell = 0
        trade_val = 0
        done = False
        while not done:
            trade_val = max(trade_val, prices[sell] - prices[buy])
            if (buy < sell and prices[sell] - prices[buy+1] > trade_val):
                # shrink window if trade can be improved
                buy += 1
            elif sell < len(prices) - 1:
                # expand if trade cannot be otherwise improved
                sell += 1
            elif buy < sell:
                buy += 1
            else:
                done = True


        return max(0, trade_val)
        


        