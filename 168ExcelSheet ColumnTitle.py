class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0 or len(prices)==1:
            return 0

        templist = []
        for i in range(1,len(prices)):
            templist.append(prices[i]-prices[i-1])

        ans = 0
        for item in templist:
            if item >0:
                ans += item

        return ans
