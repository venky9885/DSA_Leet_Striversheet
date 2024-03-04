#solved using binary search(check neetcode video)
class Solution:
    def mySqrt(self, x: int) -> int:
        f,l = 0,x
        re = 0

        while(f <= l):
            m = (f+l)//2
            if(m*m > x):
                l = m-1
                # re = m
                # m = (f+l)//2
            elif(m*m < x):
                f = m+1
                re = m
                # m = (f+l)//2
            else:
                re = m
                return m
        return re



#written by me
class Solution:
    def mySqrt(self, x: int) -> int:
        ps = 0
        for i in range(0,x+1):
            if(i*i <= x):
                ps = i
            else:
                return ps

        return ps