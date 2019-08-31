class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        count_total = 0
        for num in data:
            if num == 1:
                count_total +=1

        largest, temp = 0 , 0
        for right in range(len(data)):
            if right < count_total:
                if data[right] == 1:
                    temp +=1
            else:
                if data[right] ==1:
                    temp += 1
                if data[right-count_total] == 1:
                    temp -=1
            largest = max(largest, temp)

        return count_total - largest 
