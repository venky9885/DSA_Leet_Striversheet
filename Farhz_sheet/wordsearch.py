# https://leetcode.com/problems/word-search/

def isWord(arr,visted,r,c,word,m,n,wi):
    if(len(word) == wi):
        return True

    if(  r < 0 or c < 0 or r >= m or c >= n or word[wi] !=  arr[r][c] or visted[r][c]):
        return False
    if(arr[r][c] == word[wi]):
        visted[r][c] = True

        ans =  (
            isWord(arr,visted,r+1,c,word,m,n,wi+1) or
            isWord(arr,visted,r-1,c,word,m,n,wi+1) or
            isWord(arr,visted,r,c+1,word,m,n,wi+1) or
            isWord(arr,visted,r,c-1,word,m,n,wi+1)
        )
        visted[r][c] = False
        return ans
    # return False    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board);c  =  len(board[0])
        visted = [[False for i in range(c)] for j in range(r)]
        # print(visted)
        for i in range(r):
            for j in range(c):
                if(isWord(board,visted,i,j,word,r,c,0)):
                    return True

        
# 1. backtrack
# 2. for every (row,col) apply backtrack
# 3. track the coming path because in visted because you cant go back in forward moving path