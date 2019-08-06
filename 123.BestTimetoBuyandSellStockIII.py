class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        h1, s1, h2, s2 = -prices[0], 0, -prices[0], 0
        for price in prices:
            h1 = max(h1, -price)
            s1 = max(s1, price + h1)
            h2 = max(h2, s1-price)
            s2 = max(s2, price + h2)
        return s2
