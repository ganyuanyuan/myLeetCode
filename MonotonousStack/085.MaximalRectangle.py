class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        heights = [0 for _ in range(len(matrix[0]))]
        largest = 0
        for row in matrix:
            for i in range(len(row)):
                heights[i] = heights[i] +1 if row[i]=='1' else 0
            largest = max(largest, self.findLargest(heights))
        return largest

    def findLargest(self, heights):
        stack = []
        heights = [0] + heights + [0]
        largest = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                curr = stack.pop()
                leftBound = stack[-1]
                largest  = max(largest, heights[curr]*(i-leftBound-1))
            stack.append(i)
        return largest
