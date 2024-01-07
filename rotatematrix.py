class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ml = len(matrix)
        for i in range(ml):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(ml):
            matrix[i].reverse()


#transpose and reverse matrix
# Runtime
# Details
# 42ms
# Beats 58.43%of users with Python3
# Memory
# Details
# 17.32MB
# Beats 14.42%of users with Python3