class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        if not coins:
            return 0

        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]


        
