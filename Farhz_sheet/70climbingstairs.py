memo = {}
def clb(n):
        if( n < 0):
            return 0
        if(n == 0):
            return 1
        else:
            s1 = 0
            if(n-1 in memo):
                s1 = memo[n-1] 
            else:
                s1 = clb(n-1)
                memo[n-1] = s1
            if(n-2 in memo):
                s2 = memo[n-2]
            else:
                s2 = clb(n-2)
                memo[n-2] = s2
            
           
            
            
            return s1 + s2
#DP sol
def dp(d,n):
    if(n == 0):
        return 1
    if(n < 0 ):
        return 0

    if(d[n] != -1):
        return d[n]
    else:
        d[n] = dp(d,n-1)+dp(d,n-2)
        return d[n]

    
    
class Solution:
    
    def climbStairs(self, n: int) -> int:
        d = [-1]*(n+1)
        return dp(d,n)

        
