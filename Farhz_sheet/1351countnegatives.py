#this solution is with binary search
class Solution:
    def binarySearch(self,grid: List[List[int]],st,en,r):
        if st>en:return 0
        mid=st+(en-st)//2
        if grid[r][mid]<0:
            return en-mid+1+self.binarySearch(grid,st,mid-1,r)
        return self.binarySearch(grid,mid+1,en,r)
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            count+=self.binarySearch(grid,0,len(grid[i])-1,i)
        return count            



#it is accepted but not binary search solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        re  = []
        for i in grid:
            re.extend(i)
        re.sort()
        c = 0
        for i in re:
            if(i < 0):
                c+=1
            else:
                return c
        return c
        