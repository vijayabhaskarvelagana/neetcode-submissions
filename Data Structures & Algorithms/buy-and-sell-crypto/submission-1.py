class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get the mx_arr/sell_arr considering the i as the buying point
        mx_arr = []
        mx = 0
        n = len(prices)
        for i in range(n-1, -1, -1):
            mx = max(mx, prices[i])
            mx_arr.append(mx)
        mx_arr.reverse()
        print(f"mx_arr: {mx_arr}")
        profit = 0
        for i in range(n):
            curr_profit = mx_arr[i] - prices[i]
            profit = max(profit, curr_profit)
        return profit

        # TC -> O(n+n) -> O(n)
        # SC -> O(n)