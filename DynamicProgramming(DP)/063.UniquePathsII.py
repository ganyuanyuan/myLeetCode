class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for j in range(m):
            if obstacleGrid[j][0] == 1:
                break
            dp[j][0] = 1

        for i in range(1,m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue

                if obstacleGrid[i-1][j] != 1 and obstacleGrid[i][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif obstacleGrid[i-1][j] != 1:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i][j-1] != 1:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]
