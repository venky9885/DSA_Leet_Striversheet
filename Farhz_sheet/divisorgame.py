res =  True
def alice(n,c,dp):
    global res
    if(n < 0):
    
        return
    if(dp[n] != -1):
        res =  dp[n]
        return 
    if(c%2 != 0 and n == 1):
        print("FLS")
        res = False
        dp[n] =  False
        return
    if(c%2 == 0 and n == 1):
        print("TRU")
        res = True
        dp[n] = True
        # alice(n,0)
        return
    
    # else:
    #     return

    for x in range(1,n):
        if(n%x == 0):
            return alice(n-x,c+1,dp)

class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [-1]*(n+1)
        alice(n,1,dp)
        print(res)
        return res

        
