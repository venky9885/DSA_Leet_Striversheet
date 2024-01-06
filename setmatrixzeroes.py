class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rw = []
        cl = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    rw.append(i)
                    cl.append(j)
        
        for l in rw:
            matrix[l] = [0]*len(matrix[0])
        for k in range(len(matrix)):
            for j in cl:
                matrix[k][j] = 0

                
# Runtime
# Details
# 109ms
# Beats 83.87%of users with Python3
# Memory
# Details
# 18.12MB
# Beats 21.68%of users with Python3