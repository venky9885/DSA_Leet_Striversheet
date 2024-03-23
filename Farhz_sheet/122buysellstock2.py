class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1;ts = 0
        while(i < len(prices)):
            print(prices[i-1],prices[i])
            pf = prices[i]-prices[i-1]
            if(pf <= 0):
                i+=1
            else:
                ts+=pf
                i+=1

            # i+=1
        return ts



# Runtime
# 64
# ms
# Beats
# 51.82%
# of users with Python3
# Memory
# 18.50
# MB
# Beats
# 22.68%
# of users with Python3