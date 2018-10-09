# Submission Result: Accepted
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, buy = 0, -1
        n = len(prices)
        for i in range(n-1):
            if prices[i] < prices[i+1] and buy == -1:
                buy = prices[i]
            elif prices[i] >= prices[i+1] and buy != -1:
                profit += prices[i] - buy
                buy = -1
        if buy != -1: 
            profit += prices[-1] - buy
        return profit
