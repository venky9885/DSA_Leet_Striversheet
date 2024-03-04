#we can solve it by another way by extend to single list and bin search or for loop

#check neet code video ,using binaryb search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        # First check for row
        top,bot = 0,rows-1
        while(top <= bot):
            mid = (top+bot)//2
            #see mid val of row end value -1
            if( target > matrix[mid][-1]):
                top = mid+1
            #see mid val of row with zero
            elif(target < matrix[mid][0]):
                bot = mid-1
            else:
                break

        if(not (top <= bot)):
            print("555",top,bot)
            return False
        row =(top+bot)//2
        #then perform bin search in that row
        l,r = 0,cols-1
        while(l <= r):
            m = (l+r)//2
            if(target > matrix[row][m]):
                l = m+1
            elif(target < matrix[row][m]):
                r = m-1
            else:
                return True
        return False
        