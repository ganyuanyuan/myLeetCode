class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        largest = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                k = stack[-1]
                largest = max(largest, heights[j]*(i-k-1))
            stack.append(i)
        return largest

#############################################################################
#
#       find left smaller one and right smaller one
#              |                    |
#              k                    i
#
##############################################################################
