class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPf  = 0
        lef = 0
        rig = 1
        while(rig < len(prices)):
            if(prices[rig]>prices[lef]):
                maxPf =  max(maxPf,prices[rig]-prices[lef])
            else:
                lef = rig
            rig+=1
        print(maxPf)
        return maxPf



# Runtime
# Details
# 760ms
# Beats 93.33%of users with Python3
# Memory
# Details
# 29.31MB
# Beats 5.87%of users with Python3