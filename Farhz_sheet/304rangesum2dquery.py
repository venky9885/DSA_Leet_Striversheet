class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.W = len(matrix[0])+1
        self.H = len(matrix)+1

        self.dp = [[0 for i in range(self.W)] for _ in range(self.H)]
        # we start from index 1 because initial rows and cols have sum itself is max
        for i in range(1, self.H):
            for j in range(1, self.W):
                # The prefix sum is calculated using the formula:
                self.dp[i][j] = self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]+matrix[i-1][j-1]

# |row1col1  --- row1col2|
# |                      |
# |row2col1  --- row2col2|

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


# Ex with visuvalization
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# dp = [
#     [0, 0, 0, 0],
#     [0, 1, 3, 6],
#     [0, 5, 12, 21],
#     [0, 12, 27, 45]
# ]
#  (row1, col1) = (1, 1) to (row2, col2) = (2, 2):
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┴───┴───┘
# We want to find the sum of the region:
# ┌───┬───┐
# │ 5 │ 6 │
# ├───┼───┤
# │ 8 │ 9 │
# └───┴───┘
# sumRegion = ps[3][3] - ps[1][3] - ps[3][1] + ps[1][1]
#
