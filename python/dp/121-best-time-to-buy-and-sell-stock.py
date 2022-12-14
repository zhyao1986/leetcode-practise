from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        min_price = prices[0]
        dp = [0]*n
        for i in range(1, n):
            if prices[i] > min_price:
                dp[i] = max(dp[i-1], prices[i]-min_price)
            else:
                min_price = prices[i]
                dp[i] = dp[i-1]
        return dp[-1]
    
    def maxProfit_opt1(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        profit = 0
        for i in range(1, n):
            if prices[i] > min_price:
                profit = max(profit, prices[i] - min_price)
            else:
                min_price = prices[i]
        return profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
    print(Solution().maxProfit_opt1(prices))