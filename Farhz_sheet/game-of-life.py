# https://leetcode.com/problems/game-of-life/


def neighCount(arr,r,c,m,n):
    if(0 <= r < m and 0 <= c < n):
        return arr[r][c] 
    else:
        return 0
def ruleApply(r,c,arr,ng):
    if(arr[r][c] == 1 and (ng == 2 or ng == 3 )):
        return 1
    elif(arr[r][c] == 1  and (ng < 2)):
        return 0
    elif(arr[r][c] == 1  and (ng > 3)):
        return 0
    elif(arr[r][c] == 0  and (ng == 3)):
        return 1
    else:
        return 0
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board);n = len(board[0])
        aux = [[-1 for i in range(n) ] for _ in range(m)]
        # print(aux)
        for i in range(m):
            for j in range(n):
                ng = neighCount(board,i+1,j,m,n)+neighCount(board,i,j+1,m,n)+neighCount(board,i+1,j+1,m,n)+neighCount(board,i-1,j-1,m,n)+neighCount(board,i-1,j,m,n)+neighCount(board,i,j-1,m,n)+neighCount(board,i-1,j+1,m,n)+neighCount(board,i+1,j-1,m,n)
                # print(ng)
                aux[i][j] = ruleApply(i,j,board,ng)
        for i in range(m):
            for j in range(n):
                board[i][j] = aux[i][j]
        # return aux

        
        

# simple problem just apply rules for old board
# make sure doesnt overflow row and col and remember it row ,col exceed rule
