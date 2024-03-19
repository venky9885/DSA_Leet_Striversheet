class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(m-1):
            newrow = [1]*n
            for j in range(n-2, -1, -1):
                newrow[j] = row[j]+newrow[j+1]
            row = newrow
        return row[0]

# Bottom up approach we sum down and right for current

# Runtime
# 31
# ms
# Beats
# 92.96%
# of users with Python3
# Memory
# 17.26
# MB
# Beats
# 28.60%
# of users with Python3
