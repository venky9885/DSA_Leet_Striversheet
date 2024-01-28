# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

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


        
# For better understanding Create a graph time on +x axis

# Use 2 pointer technique
# Traverse from left to right both pointers
# always maintain left minimial ,if not possible make left as right
# from minimial calculate all profits and increment right
# stop if right reaches end