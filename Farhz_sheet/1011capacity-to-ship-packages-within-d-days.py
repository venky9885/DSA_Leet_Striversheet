#for better understanding check neetcode video
#https://www.youtube.com/watch?v=ER_oLmdc-nw

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # max is the lower boud and tot sum is upper bound
        # in this search space oerform binary search
        l,r = max(weights),sum(weights)
        res =  r
        def canShip(cap):
            ship = 1
            newcap = cap
            for i in weights:
                if(newcap - i < 0):
                    ship+=1
                    newcap = cap
                #     newcap-=i
                # else:
                newcap-=i
            return ship  <= days

        while(l<=r):
            cap = (l+r)//2
            if(canShip(cap)):
                res = min(cap,res)
                #we need minimum so reduce r(they said min capacity requireds)
                r = cap-1
            else:
                l = cap+1
        return res
                