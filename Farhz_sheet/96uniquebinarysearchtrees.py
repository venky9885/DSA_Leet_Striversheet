class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        # we will make root each time each one
        # skip this line  numTree[4] = numTree[0] + numTree[3]+
        if(n == 1 or n == 0):
            return 1
        ct = 0
        # n = 4(1,5) for 2 (2-1=1) * (4-2=2)
        #           for 3 (3-1 = 2 ) * (4-3 = 1)
        for i in range(1, n+1):
            ct += self.numTrees(i-1) * self.numTrees(n - i)
        return ct


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1  # If n is 0 or 1, there is only one unique BST possible
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: There is one unique BST with 0 nodes
        dp[1] = 1  # Base case: There is one unique BST with 1 node

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # The number of unique BSTs for i nodes is the sum of
                # the number of left subtrees and the number of right subtrees
                # where j is the root node
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
