
# check neetcode video  https://www.youtube.com/watch?v=H9bfqozjoqs
# Also this https://www.youtube.com/watch?v=SIHLJdF4F8A&t=15s better visuvalization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # here we go one by one coin and check the dp cache and we go top down approach
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            # print("------------")
            for coin in coins:
                # print(dp[i],1+dp[i-coin])
                if(i-coin >= 0):
                    # why we add 1 is we subtracted one coin and added coin count
                    dp[i] = min(dp[i], 1+dp[i-coin])

        return dp[-1] if(dp[amount] != amount+1) else -1


# Brute force dont learn thios,thjrows TLE error
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        r = []  # List to store the number of coins used for each possibility4

        def f(i, total, count):
            if i >= len(coins) or total > amount:
                return
            if total == amount:
                r.append(count)
                return

            # Choose the current coin and recurse
            f(i, total + coins[i], count + 1)

            # Move to the next coin and recurse
            f(i + 1, total, count)

        f(0, 0, 0)  # Start recursion with initial values
        return min(r) if r else -1  # Return the minimum count if r is not empty, otherwise return -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin_amt in coins:
            for target in range(coin_amt, amount + 1):
                dp[target] = min(dp[target], 1 + dp[target - coin_amt])

        return dp[amount] if dp[amount] != float('inf') else -1
