# https://leetcode.com/problems/powx-n/description/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x,n):
            if(x == 0):
                return 0
            if(n == 0):
                return 1
            return  x*calc(x*x,n//2) if(n%2) else calc(x*x,n//2)
        
        return calc(x,n) if(n > 0) else 1/calc(x,abs(n))
    


# use recursion 
# if its odd 2^3 =  2* (rec)
# else rec