class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x,n):
            if(x == 0):
                return 0
            if(n == 0):
                return 1
            return  x*calc(x*x,n//2) if(n%2) else calc(x*x,n//2)
        
        return calc(x,n) if(n > 0) else 1/calc(x,abs(n))


# Runtime
# Details
# 35ms
# Beats 76.03%of users with Python3
# Memory
# Details
# 17.46MB
# Beats 13.97%of users with Python3