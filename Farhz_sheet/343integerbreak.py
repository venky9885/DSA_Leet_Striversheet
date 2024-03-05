class Solution:
    def integerBreak(self, n: int) -> int:
        #in hint said find similaries for 7,8,9,10 => (12,18,27,36)
        # so its like num//3 gives no of 3`s and remiander is there means remove last 3 and put remainer
        if( n < 4):
            return n-1
        prod = 1
        while ( n > 4):
            prod *=3
            n-=3

        return prod*n
        