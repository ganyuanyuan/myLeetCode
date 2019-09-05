import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for i, stone in enumerate(stones):
            heapq.heappush(heap, (-stone, i))


        while len(heap)>1 :
            num1, index1= heapq.heappop(heap)
            num2, index2 = heapq.heappop(heap)
            new_num = num2 - num1
            if new_num != 0:
                heapq.heappush(heap, (-new_num, index1+index2))

        if not heap:
            return 0
        return -heapq.heappop(heap)[0]
