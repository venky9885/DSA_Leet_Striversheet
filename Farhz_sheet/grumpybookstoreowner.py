class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ls =  customers.copy()
        for i in range(len(ls)):
            if(grumpy[i] == 1):
                ls[i] = 0
        # print(ls)
        
        res = []
        res2 = []
        for i in range(len(customers)-minutes+1):
            sm  = 0
            ns = 0
            for j in range(minutes):
                # if(grumpy[i+j] == 0):
                ns+=ls[i+j]
                sm+=customers[i+j]
            res.append(sm)
            res2.append(ns)
        # print(res,res2)
        mx = 0
        # ind =  res.index(max(res))
        # print(ind)
        smp = sum(ls)

        for i in range(len(res)):
            mx =  max(smp+res[i]-res2[i],mx)
        return mx
    


# it is done on own just think it with 5 %effiency code