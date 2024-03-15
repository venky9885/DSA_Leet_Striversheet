
# this is from neetcode https://www.youtube.com/watch?v=6X7Ha2PrDmM
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # will do trecursibvley top down cache approach
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        # its easy
        # in this we will create cache with top down approach with  1+min(down, right, diag) and search for max and return its square
        # while going down cells will be pre computed sometime ,so we will add values to them

        def f(r, c):
            if(r >= ROWS or c >= COLS):
                return 0
            if((r, c) not in cache):
                down = f(r+1, c)
                right = f(r, c+1)
                diag = f(r+1, c+1)
                cache[(r, c)] = 0
                if(matrix[r][c] == "1"):
                    cache[(r, c)] = 1+min(down, right, diag)

            return cache[(r, c)]

        f(0, 0)
        return max(cache.values())**2


# this solution from leetcode
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def F(i, j):
            if i == m or j == n:
                return 0

            elif matrix[i][j] == '0':
                return 0

            elif memo[i][j] != -1:
                return memo[i][j]

            ans = min(F(i + 1, j), F(i, j + 1), F(i + 1, j + 1)) + 1
            memo[i][j] = ans
            return ans

        max_side = 0
        for i in range(m):
            for j in range(n):
                max_side = max(max_side, F(i, j))

        return max_side ** 2
