class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins :
            return -1
        if amount == 0:
            return 0

        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0

        for curr in range(amount+1):
            for coin in coins:
                if curr-coin<0 or dp[curr-coin]==-1:
                    continue
                if dp[curr] == -1 :
                    dp[curr] = dp[curr-coin] + 1
                else:
                    dp[curr] = min(dp[curr] , dp[curr-coin]+1)

        return dp[amount]
