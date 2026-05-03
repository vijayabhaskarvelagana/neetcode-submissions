class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        profit = 0
        while i<n:
            j = i+1
            while j<n:
                curr = prices[j] - prices[i]
                profit = max(profit, curr)
                j += 1
            i += 1
        return profit

        # TC -> O(n*n) -> O(n**2)
        # SC -> O(1)