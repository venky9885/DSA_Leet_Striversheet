class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == 0):
                    # if it is zero we will continue
                    continue
                if(row == 0 or col == 0):
                    # if its 1 and inital row or column we fill 1
                    # due to this step it will not throw array bound negative exptinon
                    dp[row][col] = 1
                else:
                    minimum = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1])
                    # we found one more so we add 1
                    dp[row][col] = minimum+1
        res = []
        for i in dp:
            res.extend(i)
        return sum(res)
