class Solution:
    def knightDialer(self, n: int) -> int:
        prev = [1]*10
        # dp = [[1]*10 for _ in range(n)]
        mod_num = 1000000007
        # FOR each time we will calculate all posibile movements in every position and return it
        # here we will calculate the no of possible positions for n range,as given in question see below
        # place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number
        for i in range(1, n):
            # prev = dp[i-1]
            prev = [prev[4] + prev[6], prev[6] + prev[8], prev[7] + prev[9], prev[4] + prev[8],
                    prev[0] + prev[3] + prev[9], 0, prev[0] + prev[1] + prev[7], prev[2] + prev[6],
                    prev[1] + prev[3], prev[2] + prev[4]]
            prev = [x % mod_num for x in prev]
        return sum(prev) % mod_num

    # By doing this for n iterations, the code effectively calculates all possible combinations of movements for the knight within n moves.

# Neetcode solution below


class Solution:
    def knightDialer(self, n: int) -> int:
        if(n == 1):
            return 10
        mod = 10**9+7
        # below are jumps we can amke from that position
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        dp = [1]*10  # ways to land on ith digit
        for _ in range(n-1):
            next_dp = [0]*10
            for n in range(10):
                for j in jumps[n]:
                    next_dp[j] = next_dp[j]+dp[n]
            dp = next_dp
        return sum(dp) % mod
