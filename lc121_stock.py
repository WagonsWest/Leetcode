# 买卖一次
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        min = float('INF')
        profit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < min:
                min = prices[i]
            
            max = prices[i]
            if profit < max-min:
                profit = max-min

        return profit if profit > 0 else 0