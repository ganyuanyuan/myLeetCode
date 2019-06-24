#use heap like merge k sorted arrays, and push back interval
import heapq
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if not intervals:
            return []
            
        ans = []
        heap = []
        for i in range(len(intervals)):
            if intervals[i]:
                heapq.heappush(heap, (intervals[i][0].start, intervals[i][0].end, i, 0, intervals[i][0] ))
                
        while heap:
            start, end, i, index, interval = heapq.heappop(heap)
            self.pushBack(ans, interval)
            if index+1<len(intervals[i]):
                heapq.heappush(heap, (intervals[i][index+1].start,intervals[i][index+1].end, i, index+1, intervals[i][index+1] ))
                
        return ans 
        
    def pushBack(self, ans, interval):
        if len(ans)==0:
            ans.append(interval)
            return 
            
        if interval.start> ans[-1].end:
            ans.append(interval)
            return 
        
        ans[-1].end = max(ans[-1].end, interval.end)
