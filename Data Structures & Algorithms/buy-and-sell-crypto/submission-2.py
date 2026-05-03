class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        n = len(prices)
        profit = 0
        while i<n and j<n:
            buy = prices[i]
            sell = prices[j]
            if sell > buy:
                curr_profit = sell - buy
                profit = max(profit, curr_profit)
            else:
                i = j # start selling from j index as it is the new min now
            j += 1
        return profit

        # TC -> O(n)
        # SC -> O(1)
            