
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        if not bookings:
            return [0 for _ in range(n)]

        points = []
        for start, end, k in bookings:
            points.append([start, k])
            points.append([end+1,  -k])

        points = sorted(points)
        ans = [0 for _ in range(n)]
        i,j = 1, 0
        present = 0
        while i <= n and j<len(points):
            if i < points[j][0]:
                ans[i-1] = present
                i += 1

            elif i == points[j][0]:
                present += points[j][1]
                j += 1
                ans[i-1] = present

        return ans


##################################################################################
# Sweep Line :
#    step1: using an array(points) store [start, 1] & [end,  -1]
#    step2: iterate answer or points from left to right: start-->ans+1, end-->ans-1
##################################################################################
