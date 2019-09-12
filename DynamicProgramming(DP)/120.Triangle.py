class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return None

        dp = []
        for i in range(len(triangle)):
            dp.append([None for _ in range(len(triangle[i]))])

        dp[0][0] = triangle[0][0]

        for i in range(1, len(dp)):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            for j in range(1,len(dp[i])-1):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] +triangle[i][i]

        return min(dp[-1])

#############################################################################
#
#     dfs ----> time limite
#
##############################################################################
