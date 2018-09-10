class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0 or len(prices)==1:
            return 0
        list1 = []
        for i in range(1, len(prices)):
            list1.append(prices[i]-prices[i-1])
        for i in range(0, len(list1)-1):
            if list1[i]>0:
                list1[i+1]= list1[i+1]+list1[i]

        if max(list1)>0:
            return max(list1)
        else:
            return 0
