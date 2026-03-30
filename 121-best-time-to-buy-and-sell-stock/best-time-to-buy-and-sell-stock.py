class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # left = buy, right = sell
        maxP = 0  # max profit
        
        while r < len(prices):
            # profitable transaction check
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # move left pointer to the new low
                l = r
            
            r += 1
        
        return maxP
        