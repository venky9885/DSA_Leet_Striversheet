class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        h,w = len(grid),len(grid[0])
        visted = [[False for _ in range(w)] for _ in range(h)]
        print(visted)
        
        #in this below function it search for wall or 0 so if it hits both every where
        #then returns 0
        #otherwise returns 1 by completing all

        def chk(i, j):

            if not (0 <= i < h and 0 <= j < w):
                return 0
            if grid[i][j] == '0' or visted[i][j]:
                return 0
            visted[i][j] = True
            chk(i + 1, j)
            chk(i, j + 1)
            chk(i - 1, j)
            chk(i, j - 1)
            return 1
            # if(grid[i][j] == '1' ):
            #     return 1
            
        tc = 0
        for i in range(h):
            for j in range(w):
                if(visted[i][j] == False and grid[i][j] == "1"):
                    print(chk(i,j))
                    if(chk(i,j) == 0):
                        tc+=1
        return tc
        