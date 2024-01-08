class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = 0
        while(j < len(matrix)):
            if(target  == matrix[j][-1]):
                return True
            elif(target  < matrix[j][-1]):
                for i in range(len(matrix[j])):
                    if(target == matrix[j][i]):
                        return True
                else:
                    return False
            else:
                j+=1
        return False

# Runtime
# Details
# 48ms
# Beats 69.17%of users with Python3
# Memory
# Details
# 17.86MB
# Beats 17.41%of users with Python3