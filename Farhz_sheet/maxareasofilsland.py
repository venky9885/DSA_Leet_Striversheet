# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n =  len(grid[0])


        def dfs(i,j):
            if(not (0 <= i < m and 0 <= j < n ) or grid[i][j] == 0):
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)
        res = 0
        for i in range(m):
            for j in range(n):
                sol =  dfs(i,j)
                res = max(res,sol)
        return res

# for every postion of matrix apply dfs 
#after visit make zero to avoid going back in same path back