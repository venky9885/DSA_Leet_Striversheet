class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def rc(m):
            if(m == 0):
                return False
            if(m == 1):
                return True
            if(m%2 == 0):
                return rc(m//2)
            else:
                return False
        return (rc((n)))
#or do by loop till 31 and matches 2**i
