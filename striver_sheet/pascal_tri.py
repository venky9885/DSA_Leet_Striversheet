
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        full = [[1]]
        for i in range(1,numRows):
            temp = [1]
            for j in range(1,((i+1)//2)):
                temp.append(full[i-1][j-1]+full[i-1][j])
            if((i)%2 == 0 ):
                
                ch = full[i-1][((i+1)//2)] +full[i-1][((i+1)//2)-1]
                temp.append(ch)
                temp.extend(temp[:-1][::-1])
                full.append(temp)
            else:
                temp.extend(temp[::-1])
                full.append(temp)
     
        return full



# Runtime
# Details
# 40ms
# Beats 58.92%of users with Python3
# Memory
# Details
# 17.42MB
# Beats 11.09%of users with Python3