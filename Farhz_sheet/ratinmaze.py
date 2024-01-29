class Solution:
    def findPath(self, m, n):
        r = len(m)
        c = len(m[0])
        
        vis = [[0 for _ in range(c)] for _ in range(r)]
        res = []
        
        def fma(i, j, s):
            nonlocal res
            
            if not (0 <= i < r and 0 <= j < c) or vis[i][j] == 1 or m[i][j] == 0:
                return
            
            if i == r - 1 and j == c - 1 and m[i][j] == 1:
                res.append(s)
                return
            
            vis[i][j] = 1
            
            fma(i + 1, j, s + 'D')
            fma(i, j + 1, s + 'R')
            fma(i - 1, j, s + 'U')
            fma(i, j - 1, s + 'L')
            
            vis[i][j] = 0
        
        # Check if the destination cell is reachable
        # if m[r - 1][c - 1] == 0:
        #     return ['-1']
        
        fma(0, 0, '')
        
        if not res:
            return ['-1']
        
        return sorted(res)


#its easy and check rules properly
#https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
